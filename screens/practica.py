import argparse
import copy
import csv
import threading
import time
import cv2 as cv
import mediapipe as mp
from utils import cvfpscalc
from utils import draw
from utils import landmark
from model.HandClassifier.HandClassifier import handClassifier

from PIL import Image, ImageTk

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import prueba_pyqt5 
import sys
width = 2040
height = 1400
dirImagenes = 'C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes'
colorFondo = QColor(135,206,250)


class ScreenPractica(QMainWindow):
        
    def __init__(self):
        super().__init__()
        self.title = 'Práctica Libre'
        self.width = width
        self.height = height
        self.initUI()
    

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana
        palette = QPalette()
        palette.setColor(QPalette.Window, colorFondo)
        self.setPalette(palette)
        self.menuBar().setNativeMenuBar(False)
        # Crea una instancia de QCamera y QCameraViewfinder
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(QSize(int(width)- 70 , int(height)))
        #1920 x 1080
        self.viewfinder.move(int(self.width / 2) - int(self.viewfinder.width() / 2),
                             int(self.height / 2) - int(self.viewfinder.height() / 2))
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

# Botón 'activar'
        # Botón 'activar'
        self.button = QPushButton('ACTIVAR SUBTITULOS', self)
        self.button.setFixedSize(QSize(600, 100))
        self.button.clicked.connect(self.activateVideo)
        self.button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        self.button.move(10, 10)

        layout = QVBoxLayout()
        layout.addWidget(self.viewfinder)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Inicializar variables y objetos necesarios para el procesamiento de imágenes
        self.hand_classifier = handClassifier()
        self.capture_timer = QTimer(self) # Establecer la frecuencia de actualización (en milisegundos)
    

        
    # Botón 'Volver'
        back_button = QPushButton('VOLVER', self)
        back_button.setFixedSize(QSize(500, 100))
        back_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width/2) + int(self.width/4), 10)

        self.show()

    def activateVideo(self):
        self.camera.start()

    

    def closeEvent(self, event):
        self.camera.stop()
        event.accept()    
    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = prueba_pyqt5.App()
        self.previous_screen.show()


#----------------------------------------------------
video = None
locker = threading.Event()
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

def time_Captured(char, times):
    global timesCaptured
    global prevChar
    global subtitle
    if timesCaptured == 10:
        subtitle += char
    if char == prevChar:
        times += 1
        return times
    else:
        prevChar = char
        return 0
    


def video_stream():
        global video
        global locker
        # Parsing de Argumentos #################################################################
        args = get_args()
        use_static_image_mode = args.use_static_image_mode
        min_detection_confidence = args.min_detection_confidence
        min_tracking_confidence = args.min_tracking_confidence    
        mp_hands = mp.solutions.hands
        
        hands = mp_hands.Hands(static_image_mode = use_static_image_mode,
            max_num_hands = 1,
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
        # Preparar la Camara
        while True:
            locker.wait()
            time.sleep(1)
            getVideo(hands,keypoint_classifier_labels, hand_classifier, cvFpsCalc, True)

        
def getVideo(hands, keypoint_classifier_labels, hand_classifier, cvFpsCalc, use_brect):
    global timesCaptured
    global video
    
    #Capturar Camara #################################
    while True:
        fps = cvFpsCalc.get()   
        ret, image = video.read()
        if ret == True:
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
                    debug_image = draw.draw_bounding_rect(use_brect, debug_image, brect)
                    debug_image = draw.draw_landmarks(debug_image, landmark_list)
                    timesCaptured = time_Captured(str(keypoint_classifier_labels[mano_senial_id]),timesCaptured)
                    debug_image = draw.draw_info_text(
                        debug_image,
                        brect,
                        handness,
                        keypoint_classifier_labels[mano_senial_id]
                    )
                    
                    textsize = cv.getTextSize(subtitle, cv.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
                    textX = (debug_image.shape[1] - textsize[0]) / 2
                    debug_image = cv.putText(
                        debug_image,
                        subtitle,
                        (int(textX),450),
                        cv.FONT_HERSHEY_SIMPLEX,
                        1,
                        (255,255,0),
                        2,
                        cv.LINE_AA
                    )
            debug_image = draw.draw_info(debug_image, fps)
            debug_image = cv.resize(debug_image,(840,485))
            debug_image_tk = cv.cvtColor(debug_image, cv.COLOR_BGR2RGB)
            img = Image.fromarray(debug_image_tk)
            image = ImageTk.PhotoImage(image=img)
        else:
            print('img no capturada')
            break
#-----------------------------------------------------
