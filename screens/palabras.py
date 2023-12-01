from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

import prueba_pyqt5 
from screens import modulos
from screens import realizar_clase

width = 2040
height = 1400
dirImagenes = 'C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes'
colorFondo = QColor(135,206,250)

class ScreenPalabras(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Palabras'
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

        label = QLabel('Palabras', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(900, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;font-weight: bold;    color: #00416A;")

        clase1_button = QPushButton('Clase 1', self)
        clase1_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase1_button.setFixedSize(QSize(500, 200))
        clase1_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 230)
        clase1_button.clicked.connect(self.class1)    

        clase2_button = QPushButton('Clase 2', self)
        clase2_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase2_button.setFixedSize(QSize(500, 200))
        clase2_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 450)
        clase2_button.clicked.connect(self.class2)    

        clase3_button = QPushButton('Clase 3', self)
        clase3_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase3_button.setFixedSize(QSize(500, 200))
        clase3_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 670)
        clase3_button.clicked.connect(self.class3)    

        clase4_button = QPushButton('Clase 4', self)
        clase4_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase4_button.setFixedSize(QSize(500, 200))
        clase4_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 890)
        clase4_button.clicked.connect(self.class4)    

        clase5_button = QPushButton('Clase 5', self)
        clase5_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase5_button.setFixedSize(QSize(500, 200))
        clase5_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 1110)
        clase5_button.clicked.connect(self.class5)      

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(200, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(200, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) + int(back_button.width()) + 600 ,30)

        self.show()

    def class1(self):
        print('Clase 1 seleccionada')
        container = QPushButton('Clase 1', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase1palabras.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px;font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
        

    def class2(self):
        print('Clase 2 seleccionada')
        container = QPushButton('Clase 2', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase2palabras.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px;font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class3(self):
        print('Clase 3 seleccionada')
        container = QPushButton('Clase 3', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase3palabras.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold;border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class4(self):
        print('Clase 4 seleccionada')
        container = QPushButton('Clase 4', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase4palabras.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px;font-weight: bold;border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
    
    def class5(self):
        print('Clase 5 seleccionada')
        container = QPushButton('Clase 5', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase5palabras.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px;font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def iniciarClase(self):
        print('Clase iniciada')
        self.next_screen = realizar_clase.ScreenRealizarClase()
        self.next_screen.show()
        self.hide()

    def show_next_screen(self):
        self.next_screen = prueba_pyqt5.App()
        self.next_screen.show()
        self.hide()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = modulos.ScreenModulos()
        self.previous_screen.show()