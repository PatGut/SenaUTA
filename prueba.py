import sys
import cv2
import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from mediapipe import solutions as mp
from model.HandClassifier.HandClassifier import handClassifier

class SignLanguageRecognition(QMainWindow):
    def __init__(self, device=0, width=960, height=540, parent=None):
        super(SignLanguageRecognition, self).__init__(parent)

        self.device = device
        self.width = width
        self.height = height
        self.video_capture = cv2.VideoCapture(self.device)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self.mp_hands = mp.hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )

        self.hand_classifier = handClassifier()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self.central_widget)
        layout.addWidget(self.video_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Actualizar cada 30 ms

        self.subtitle = ''
        self.times_captured = 0
        self.prev_char = ''

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.mp_hands.process(frame)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    brect = self.calc_bounding_rect(frame, hand_landmarks)
                    landmark_list = self.calc_landmark_list(frame, hand_landmarks)
                    pre_processed_landmark_list = self.pre_process_landmark(landmark_list)
                    mano_senial_id = self.hand_classifier(pre_processed_landmark_list)

                    frame = self.draw_bounding_rect(True, frame, brect)
                    frame = self.draw_landmarks(frame, landmark_list)
                    frame = self.draw_info_text(frame, brect, mano_senial_id)

            frame = cv2.resize(frame, (840, 485))
            height, width, channel = frame.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.video_label.setPixmap(pixmap)

    def calc_bounding_rect(self, image, hand_landmarks):
        landmark_list = self.calc_landmark_list(image, hand_landmarks)
        x, y, w, h = cv2.boundingRect(np.array(landmark_list))
        return x, y, w, h

    def calc_landmark_list(self, image, hand_landmarks):
        return [(int(point.x * image.shape[1]), int(point.y * image.shape[0])) for point in hand_landmarks.landmark]

    def pre_process_landmark(self, landmark_list):
        # Aquí puedes agregar cualquier preprocesamiento adicional necesario
        return landmark_list

    def draw_bounding_rect(self, use_brect, image, brect):
        if use_brect:
            x, y, w, h = brect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image

    def draw_landmarks(self, image, landmark_list):
        for point in landmark_list:
            cv2.circle(image, point, 5, (255, 0, 0), -1)
        return image

    def draw_info_text(self, image, brect, mano_senial_id):
        x, y, _, _ = brect
        textsize = cv2.getTextSize(str(mano_senial_id), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        textX = (image.shape[1] - textsize[0]) // 2
        cv2.putText(image, str(mano_senial_id), (int(textX), y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2,
                    cv2.LINE_AA)
        self.update_subtitle(str(mano_senial_id))
        return image

    def update_subtitle(self, char):
        if self.times_captured == 10:
            self.subtitle += char
        if char == self.prev_char:
            self.times_captured += 1
        else:
            self.prev_char = char
            self.times_captured = 0

    def closeEvent(self, event):
        self.video_capture.release()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignLanguageRecognition()
    window.setGeometry(200, 200, 1000, 680)
    window.setWindowTitle("Reconocimiento del lenguaje de señas chileno")
    window.show()
    sys.exit(app.exec_())

