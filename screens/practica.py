import argparse
import copy
import csv
import cv2 as cv
import mediapipe as mp
from utils import cvfpscalc
from utils import draw
from utils import landmark
from model.HandClassifier.HandClassifier import handClassifier
from PyQt5.QtWidgets import  QMainWindow, QPushButton, QLabel,  QDesktopWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import QImage, QPixmap, QPalette, QColor, QFont
from PyQt5.QtCore import  QSize, QThread, pyqtSignal
import proyectoQt5 

colorFondo = QColor(135,206,250)

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(QImage)
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.subtitle = ''
        self.timesCaptured = 0
        self.prevChar = ''
        self.video = None
        self.width, self.height = self.get_screen_resolution()
    
    def get_screen_resolution(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        return screen_rect.width(), screen_rect.height()
    
    def time_Captured(self, char, times):
        if self.timesCaptured == 10:
            self.subtitle += char
        if char == self.prevChar:
            times += 1
            return times
        else:
            self.prevChar = char
            return 0
    
    def stop(self):
        self.running = False  # Añadir un atributo para controlar el bucle

    def run(self):
        self.running = True
        args = self.args # Asegúrate de que get_args() está definida y devuelve los argumentos correctos
        self.video = cv.VideoCapture(args.device)
        self.video.set(cv.CAP_PROP_FRAME_WIDTH, args.width)
        self.video.set(cv.CAP_PROP_FRAME_HEIGHT, args.height)
        use_static_image_mode = args.use_static_image_mode
        min_detection_confidence = args.min_detection_confidence
        min_tracking_confidence = args.min_tracking_confidence    
        mp_hands = mp.solutions.hands
        
        hands = mp_hands.Hands(static_image_mode = use_static_image_mode,
            max_num_hands = 2,
            min_detection_confidence = min_detection_confidence,
            min_tracking_confidence = min_tracking_confidence
        )

        # Insertar modelo de clasificación
        
        hand_classifier = handClassifier()
        
        #Leer Labels
        with open('model/HandClassifier/hand_label.csv',
                encoding='utf-8-sig') as f:
            keypoint_classifier_labels = csv.reader(f)
            keypoint_classifier_labels = [
                row[0] for row in keypoint_classifier_labels
            ]
        # medir FPS
        cvFpsCalc = cvfpscalc.CvFpsCalc(buffer_len=10)
          # Asumiendo que usas la primera cámara
        while self.running:
            fps = cvFpsCalc.get() 
            ret, image = self.video.read()
            if not ret:
                break

            image = cv.flip(image, 1) # Mostrar espejo de la camara
            debug_image = copy.deepcopy(image)
            #Funciona mejor con imagen a color
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            if results.multi_hand_landmarks is not None:
                for hand_landmarks,handness in zip(results.multi_hand_landmarks,
                                                results.multi_handedness):
                    # calcular bordes de las manos
                    brect = landmark.calc_bounding_rect(debug_image, hand_landmarks)
                    # Calcular Puntos de referencias
                    landmark_list = landmark.calc_landmark_list(debug_image, hand_landmarks)
                    #Convertir a cordenadas relativas / normalizada
                    pre_processed_landmark_list = landmark.pre_process_landmark(
                        landmark_list)
                    #Clasificación de la mano
                    mano_senial_id = hand_classifier(pre_processed_landmark_list)
                    #Dibujar
                    debug_image = draw.draw_bounding_rect(True, debug_image, brect)
                    debug_image = draw.draw_landmarks(debug_image, landmark_list)
                    self.timesCaptured = self.time_Captured(str(keypoint_classifier_labels[mano_senial_id]), self.timesCaptured)
                    debug_image = draw.draw_info_text(
                        debug_image,
                        brect,
                        handness,
                        keypoint_classifier_labels[mano_senial_id]
                    )
                    
                    textsize = cv.getTextSize(self.subtitle, cv.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
                    textX = (debug_image.shape[1] - textsize[0]) / 2
                    debug_image = cv.putText(
                        debug_image,
                        self.subtitle,
                        (int(textX),450),
                        cv.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255,255,0),
                        2,
                        cv.LINE_AA
                    )
                
            debug_image = draw.draw_info(debug_image, fps)
            debug_image = cv.resize(debug_image,(int(self.width), int(self.height - self.height*0.1)))

            # Convertir el frame a formato QImage
            rgb_image = cv.cvtColor(debug_image, cv.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Emitir la señal
            self.change_pixmap_signal.emit(convert_to_Qt_format)
        
        self.video.release()


class ScreenPractica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Práctica Libre'
        self.width, self.height = self.get_screen_resolution()
        self.initUI()
#Funcion para obtener la resolución de la pantalla
    def get_screen_resolution(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        return screen_rect.width(), screen_rect.height()
#Funcion para sombreado de botones
    def add_shadow_effect(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(10, 10)
        widget.setGraphicsEffect(shadow)
#UI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        self.setFixedSize(self.size())

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(135, 206, 250))
        self.setPalette(palette)
        self.menuBar().setNativeMenuBar(False)

        # Botón 'Volver'
        back_button = QPushButton('VOLVER', self)
        back_button.setFixedSize(QSize(int(self.width / 5.1), int(self.height / 16)))
        back_button_border_width_percentage = 0.009
        back_button_border_width = int(self.height * back_button_border_width_percentage)
        back_button.setStyleSheet(
            f"border: {back_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        back_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.013))
        back_button_font.setBold(True)
        back_button.setFont(back_button_font)
        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 1.25), int(self.height / 160))
        self.add_shadow_effect(back_button)
        
    #Hilos
        # Inicializar QLabel para mostrar el video
        self.image_label = QLabel(self)
        self.image_label.resize(int(self.width), int(self.height - self.height*0.1))  # Ajusta el tamaño según tus necesidades
        self.image_label.move(0,int(back_button.height()*1.5))  # Ajusta la posición según tus necesidades
    
        args = ScreenPractica.get_args()  # Asegúrate de que esta función devuelva los argumentos necesarios
        self.thread = VideoThread(args)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
        
        self.showFullScreen()
        self.show()

#Funciones para actualizar la imagen y obtener datos
    def update_image(self, cv_img):
        qt_img = QPixmap.fromImage(cv_img)
        self.image_label.setPixmap(qt_img)  # Asegúrate de que image_label está definido
    
    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("--device", type=int, default=0)
        parser.add_argument("--width", help='cap width', type=int, default=960)
        parser.add_argument("--height", help='cap height', type=int, default=540)

        parser.add_argument('--use_static_image_mode', action='store_false')
        parser.add_argument("--min_detection_confidence",
                            help='min_detection_confidence',
                            type=float,
                            default=0.7)
        parser.add_argument("--min_tracking_confidence",
                            help='min_tracking_confidence',
                            type=int,
                            default=0.5)
        args = parser.parse_args()
        return args
    
#Cambio de pantalla y detener camara
    def back_to_previous_screen(self):
        # Detener el thread de video
        if self.thread.isRunning():
            self.thread.stop()
        
        self.previous_screen = proyectoQt5.App()
        self.previous_screen.show()
        self.hide()
