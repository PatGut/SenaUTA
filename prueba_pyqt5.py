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
import sys
from screens import modulos
from screens import practica
width = 2040
height = 1400
dirImagenes = 'C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes'
colorFondo = QColor(135,206,250)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Inicio'
        self.width = width
        self.height = height  # Define las dimensiones deseadas
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)        
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana


        # Cambiar el color de fondo a #F3E5AB
        palette = QPalette()
        palette.setColor(QPalette.Window, colorFondo)
        self.setPalette(palette)
        # Imagen con url
        label = QLabel(self)
        pixmap = QPixmap(dirImagenes+'/SeñaUta.png')
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())
        # Calcular la posición central
        center_x = int((self.width - pixmap.width()) / 2)
        center_y = int((self.height - pixmap.height()) / 2 - 400)
        # Mover la imagen a la posición central
        label.move(center_x, center_y)

        # Botón para cambiar a la siguiente pantalla
        clases_button = QPushButton('Clases', self)
        clases_button.setStyleSheet("font-family: Century Gothic;  font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clases_button.setFixedSize(QSize(500, 200))
        clases_button.move(int(self.width / 2) - int(clases_button.width() / 2), int(self.height / 2) - int(clases_button.height()))
        clases_button.clicked.connect(self.show_next_screen)

        # Botón para cambiar a la pantalla de prueba
        prueba_button = QPushButton('Prueba', self)
        prueba_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        prueba_button.setFixedSize(QSize(500, 200))
        print(int(self.height / 2) + int(prueba_button.height()) + 20)
        prueba_button.move(int(self.width / 2) - int(prueba_button.width() / 2), int(self.height / 2) + 20)
        prueba_button.clicked.connect(self.show_prueba_screen)

        # Botón para salir del programa
        #exit_button_icon = QIcon()#dirImagenes+'/salir.png'
        exit_button = QPushButton('Salir', self)
        exit_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A;")
        exit_button.setFixedSize(QSize(500, 200))        
        #exit_button.setIcon(exit_button_icon)
        # Establecer el tamaño del icono
        #exit_button.setIconSize(QSize(160, 160))
        exit_button.move(int(self.width / 2) - int(exit_button.width() / 2), int(self.height / 2) + int(prueba_button.height()) + 40)
        exit_button.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    def show_next_screen(self):
        self.next_screen = modulos.ScreenModulos()
        self.next_screen.show()
        self.hide()

    def show_prueba_screen(self):
        self.next_screen = practica.ScreenPractica()
        self.next_screen.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())