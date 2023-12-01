from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

import prueba_pyqt5 
from screens import abc
from screens import frases
from screens import palabras

width = 2040
height = 1400
dirImagenes = 'C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes'
colorFondo = QColor(135,206,250)

class ScreenModulos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Módulos'
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

        # Agregar la etiqueta 'modulos' al layout
        label = QLabel('Módulos', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(500, 200))

        label.setStyleSheet("font-family: Century Gothic;font-weight: bold;  padding-left: 50px; font-size: 100px;  color: #00416A;")

        # Cargar la imagen
        self.button_icon = QIcon(dirImagenes+'/abecedario.png')

        # Crear el botón y establecer la etiqueta
        self_button = QPushButton(self)
        self_button.setFixedSize(QSize(600, 500))
        self_button.setIcon(self.button_icon)
        self_button.clicked.connect(self.class1)
        # Establecer el tamaño del icono
        self_button.setIconSize(QSize(500, 400))
        # Establecer el margen inferior del texto en el botón
        self_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; background-color: #BFF5F5; color: #00416A; ")

        self_button.move(int(self.width / 3) - int(self_button.width()) + 250,230)

        # Botón 'clase 2'
        button2_icon = QIcon(dirImagenes+'/palabras.png')
        button2 = QPushButton(self)
        button2.setFixedSize(QSize(750, 500))
        button2.setIcon(button2_icon)
        # Establecer el tamaño del icono
        button2.setIconSize(QSize(650, 400))
        button2.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        button2.clicked.connect(self.class2)
        button2.move(int(self.width / 2) - int(self_button.width() / 2)+ 250,230)

        # Botón 'clase 3'
        button3_icon = QIcon(dirImagenes+'/frases.png')
        button3 = QPushButton(self)
        button3.setFixedSize(QSize(960, 500))
        button3.setIcon(button3_icon)
        # Establecer el tamaño del icono
        button3.setIconSize(QSize(800, 500))
        button3.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        button3.clicked.connect(self.class3)
        button3.move(int(self.width / 3) - int(self_button.width()) + 250,770)

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(400, 500))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(400, 400))
        back_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: black; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) + int(button3.width()/2) - 170,770)

        self.show()

    def class1(self):
        print('Módulo ABC seleccionado')
        self.next_screen = abc.ScreenABC()
        self.next_screen.show()
        self.hide()

    def class2(self):
        print('Módulo Palabras seleccionado')
        self.next_screen = palabras.ScreenPalabras()
        self.next_screen.show()
        self.hide()
    
    def class3(self):
        print('Módulo Frases seleccionado')
        self.next_screen = frases.ScreenFrases()
        self.next_screen.show()
        self.hide()

        

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = prueba_pyqt5.App()
        self.previous_screen.show()