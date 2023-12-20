import copy
import csv
import cv2 as cv
import mediapipe as mp
from utils import cvfpscalc
from utils import draw
from utils import landmark
from model.HandClassifier.HandClassifier import handClassifier
from PyQt5.QtWidgets import  QDesktopWidget
from PyQt5.QtGui import QImage, QColor
from PyQt5.QtCore import  QThread, pyqtSignal

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
        self.subtitle = ''
        self.timesCaptured = 0
        self.prevChar = ''
    
    def get_screen_resolution(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        return screen_rect.width(), screen_rect.height()
    
    def time_Captured(self, char, letra):
        # Cambia el subtítulo basado en la comparación entre char y letra
        if char == letra:
            self.subtitle = "CORRECTO"
        else:
            self.subtitle = "Intentalo de nuevo"
            self.prevChar = char  # Actualizar el carácter previo
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
                    self.timesCaptured = self.time_Captured(str(keypoint_classifier_labels[mano_senial_id]), args.letra)
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
            debug_image = cv.resize(debug_image,(int(self.width / 2.8), int(self.height / 2.2)))

            # Convertir el frame a formato QImage
            rgb_image = cv.cvtColor(debug_image, cv.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Emitir la señal
            self.change_pixmap_signal.emit(convert_to_Qt_format)
        
        self.video.release()
