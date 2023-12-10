import argparse
import copy
import csv
import threading
import time
import cv2 as cv
import mediapipe as mp
import numpy as np
from utils import cvfpscalc
from utils import draw
from utils import landmark
from model.HandClassifier.HandClassifier import handClassifier
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDesktopWidget, QGraphicsDropShadowEffect, QGridLayout
from PyQt5.QtGui import QImage, QPixmap, QPalette, QColor, QIcon, QFont, QPainter
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer, QThread, pyqtSignal, QObject
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import prueba_pyqt5 
import sys
colorFondo = QColor(135,206,250)
class VideoSignal(QObject):
    frame_update_signal = pyqtSignal(object)

class VideoThread(QThread):
    
    frame_signal = pyqtSignal(np.ndarray)

    def __init__(self, hand_tracking):
        super().__init__()
        self.hand_tracking = hand_tracking
        print("en videoThread")

    def run(self):
        print("Antes de run en VideoThread")
        self.hand_tracking.video_stream(self.frame_signal)

class HandTrackingFunctions:
    def __init__(self):
        self.subtitle = ''
        self.timesCaptured = 0
        self.prevChar = ''
        self.video = None
        self.locker = threading.Event()
        self.video_signal = VideoSignal()

    def create_space(self):
        self.subtitle += ' '

    def time_captured(self, char):
        print("En time_captured")
        if self.timesCaptured == 10:
            self.subtitle += char
        if char == self.prevChar:
            self.timesCaptured += 1
        else:
            self.prevChar = char
            self.timesCaptured = 0

    def erase_subtitle(self):
        self.subtitle = ''

    def get_args(self):
        print("en get_args")
        parser = argparse.ArgumentParser()
        parser.add_argument("--device", type=int, default=0)
        parser.add_argument("--width", help='cap width', type=int, default=960)
        parser.add_argument("--height", help='cap height', type=int, default=540)
        parser.add_argument('--use_static_image_mode', action='store_false')
        parser.add_argument("--min_detection_confidence", help='min_detection_confidence', type=float, default=0.7)
        parser.add_argument("--min_tracking_confidence", help='min_tracking_confidence', type=int, default=0.5)
        args = parser.parse_args()
        return args

    def get_video(self, hands, keypoint_classifier_labels, hand_classifier, cvFpsCalc, use_brect, frame_signal):
        cvFpsCalc = cvfpscalc.CvFpsCalc(buffer_len=10)
        print("Antes del while en get_video")
        while True:
            print("inicio while en get_video")
            fps = cvFpsCalc.get()
            ret, image = self.video.read()

            if ret:
                print("inicio de if ret")
                image = cv.flip(image, 1)
                debug_image = copy.deepcopy(image)
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True

                if results.multi_hand_landmarks is not None:
                    print("en if results.multi_hand_landmarks is not None")
                    for hand_landmarks, handness in zip(results.multi_hand_landmarks, results.multi_handedness):
                        print("inicio del for")
                        brect = landmark.calc_bounding_rect(debug_image, hand_landmarks)
                        landmark_list = landmark.calc_landmark_list(debug_image, hand_landmarks)
                        pre_processed_landmark_list = landmark.pre_process_landmark(landmark_list)
                        mano_senial_id = hand_classifier(pre_processed_landmark_list)

                        debug_image = draw.draw_bounding_rect(use_brect, debug_image, brect)
                        debug_image = draw.draw_landmarks(debug_image, landmark_list)
                        self.time_captured(str(keypoint_classifier_labels[mano_senial_id]))
                        debug_image = draw.draw_info_text(debug_image, brect, handness,
                                                          keypoint_classifier_labels[mano_senial_id])

                        textsize = cv.getTextSize(self.subtitle, cv.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
                        textX = (debug_image.shape[1] - textsize[0]) / 2
                        debug_image = cv.putText(debug_image, self.subtitle, (int(textX), 450),
                                                 cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv.LINE_AA)

                    debug_image = draw.draw_info(debug_image, fps)
                    debug_image = cv.resize(debug_image, (840, 485))
                    print("despues del debug_image")
                    # Emitir señal con el fotograma procesado
                    frame_signal.emit(debug_image)

                else:
                    print('No se detectaron manos en la imagen')
                    break

    def video_stream(self, frame_signal):
        print("en video_stream")
        args = self.get_args()
        use_static_image_mode = args.use_static_image_mode
        min_detection_confidence = args.min_detection_confidence
        min_tracking_confidence = args.min_tracking_confidence
        mp_hands = mp.solutions.hands

        hands = mp_hands.Hands(static_image_mode=use_static_image_mode,
                               max_num_hands=2,
                               min_detection_confidence=min_detection_confidence,
                               min_tracking_confidence=min_tracking_confidence)

        hand_classifier = handClassifier()

        with open('model/HandClassifier/hand_label.csv', encoding='utf-8-sig') as f:
            keypoint_classifier_labels = csv.reader(f)
            keypoint_classifier_labels = [row[0] for row in keypoint_classifier_labels]

        cvFpsCalc = cvfpscalc.CvFpsCalc(buffer_len=10)

        while True:
            print("en while en video_stream")
            self.locker.wait()
            time.sleep(1)
            self.get_video(hands, keypoint_classifier_labels, hand_classifier, cvFpsCalc, True, frame_signal)

    def activate_video(self):
        print("en activate_video")
        args = self.get_args()
        cap_device = args.device
        cap_width = args.width
        cap_height = args.height
        self.video = cv.VideoCapture(cap_device)
        self.video.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
        self.video.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)
        self.locker.set()
        return

    def quit_video(self):
        self.video.release()
        self.locker.clear()
        return

    def main(self):
        print("en main")
        thread_video = threading.Thread(target=self.video_stream, args=(self.video_signal,))
        thread_video.daemon = True
        self.locker.clear()
        thread_video.start()

class ScreenPractica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Práctica Libre'
        self.width, self.height = self.get_screen_resolution()
        self.hand_tracking = HandTrackingFunctions()

        # Crear una instancia de VideoThread y conectar su señal a una ranura en esta clase
        self.video_thread = VideoThread(self.hand_tracking)
        self.video_thread.frame_signal.connect(self.update_video_frame)
        self.video_thread.start()

        self.initUI()

    def get_screen_resolution(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        return screen_rect.width(), screen_rect.height()

    def add_shadow_effect(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(10, 10)
        widget.setGraphicsEffect(shadow)

    def update_video_frame(self, frame):
        try:
            q_image = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QImage.Format_RGB888)
            self.hand_tracking.video_signal.frame_update_signal.emit(q_image)
        except Exception as e:
            print(f"Error en update_video_frame: {e}")


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        self.setFixedSize(self.size())
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(135, 206, 250))
        self.setPalette(palette)
        self.menuBar().setNativeMenuBar(False)

        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(QSize(int(self.width), int(self.height / 2)))
        self.viewfinder.move(int(self.width - self.width), int(self.height / 25))
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()
        self.hand_classifier = handClassifier()
        self.capture_timer = QTimer(self)

        # Botón 'activar'
        self.button = QPushButton('ACTIVAR SUBTITULOS', self)
        self.button.setFixedSize(QSize(int(self.width / 4), int(self.height / 16)))
        self.button.clicked.connect(self.hand_tracking.activate_video)
        self.button.move(int(self.width / 256), int(self.height / 160))
        self.button_border_width_percentage = 0.009
        self.button_border_width = int(self.height * self.button_border_width_percentage)
        self.button.setStyleSheet(
            f"border: {self.button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        self.button_font = QFont("Century Gothic", pointSize=int(self.height * 0.013))
        self.button_font.setBold(True)
        self.button.setFont(self.button_font)
        self.add_shadow_effect(self.button)

        layout = QVBoxLayout()
        layout.addWidget(self.viewfinder)

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
        back_button.clicked.connect(self.hand_tracking.quit_video)
        back_button.move(int(self.width / 1.25), int(self.height / 160))
        self.add_shadow_effect(back_button)

        self.showFullScreen()
        self.show()


    def closeEvent(self, event):
        self.camera.stop()
        event.accept()    
    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = prueba_pyqt5.App()
        self.previous_screen.show()
