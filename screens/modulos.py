from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDesktopWidget, QGraphicsDropShadowEffect, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

import proyectoQt5 
from proyectoQt5 import dirImagenes
from screens import abc
from screens import frases
from screens import palabras

colorFondo = QColor(135,206,250)

class ScreenModulos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Módulos'
        self.width, self.height = self.get_screen_resolution()
        self.initUI()
    #Aqui se toma la resolución de la pantalla del usuario
    def get_screen_resolution(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        return screen_rect.width(), screen_rect.height()
    
    #Función para agregar sombreado a los botones
    def add_shadow_effect(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(20)  # Ajusta el radio de desenfoque según tus necesidades
        shadow.setColor(QColor(0, 0, 0, 150))  # Ajusta el color y la opacidad de la sombra
        shadow.setOffset(10, 10)  # Ajusta el desplazamiento de la sombra
        widget.setGraphicsEffect(shadow)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana
        palette = QPalette()
        palette.setColor(QPalette.Window, colorFondo)
        self.setPalette(palette)
        
        # Agregar la etiqueta 'modulos' al layout
        label = QLabel('MÓDULOS', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(int(self.width/4.2), int(self.height/6.3)))
        label.setStyleSheet("font-family: Century Gothic;font-weight: bold;  padding-left: 50px; font-size: 100px;  color: #00416A;")

        # Cargar la imagen
        abc_button_icon = QIcon(dirImagenes+'/abecedario.png')
        # Crear el botón y establecer la etiqueta
        abc_button = QPushButton(self)        
        abc_button.setFixedSize(QSize(int(self.width/4), int(self.height/3)))
        abc_button.setIcon(abc_button_icon)
        abc_button.clicked.connect(self.class1)
        # Establecer el tamaño del icono
        abc_button.setIconSize(QSize(int(self.width/5), int(self.height/4)))
        # Establecer el margen inferior del texto en el botón
        abc_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        abc_button_border_width = int(self.height * abc_button_border_width_percentage)
        abc_button.setStyleSheet(f"border: {abc_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        self.add_shadow_effect(abc_button)   
        abc_button.move(int(self.width / 5.5),int(self.height / 7))

        # Botón 'palabras'
        palabras_button_icon = QIcon(dirImagenes+'/palabras.png')
        palabras_button = QPushButton(self)
        palabras_button.setFixedSize(QSize(int(self.width/3.5), int(self.height/3)))
        palabras_button.setIcon(palabras_button_icon)
        palabras_button.clicked.connect(self.class2)
        # Establecer el tamaño del icono
        palabras_button.setIconSize(QSize(int(self.width/4), int(self.height/4)))
        # Establecer el margen inferior del texto en el botón
        palabras_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        palabras_button_border_width = int(self.height * palabras_button_border_width_percentage)
        palabras_button.setStyleSheet(f"border: {palabras_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        self.add_shadow_effect(palabras_button)   
        palabras_button.move(int(self.width / 2.1),int(self.height / 7))
        

        # Botón 'clase 3'
        frases_button_icon = QIcon(dirImagenes+'/frases.png')
        frases_button = QPushButton(self)
        frases_button.setFixedSize(QSize(int(self.width/2.7), int(self.height/3)))
        frases_button.setIcon(frases_button_icon)
        frases_button.clicked.connect(self.class3)
        # Establecer el tamaño del icono
        frases_button.setIconSize(QSize(int(self.width/3), int(self.height/3)))
        # Establecer el margen inferior del texto en el botón
        frases_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        frases_button_border_width = int(self.height * frases_button_border_width_percentage)
        frases_button.setStyleSheet(f"border: {frases_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        self.add_shadow_effect(frases_button)   
        frases_button.move(int(self.width / 5.5),int(self.height / 2))

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(int(self.width/6), int(self.height/3)))        
        back_button.setIcon(back_button_icon)
        back_button.clicked.connect(self.back_to_previous_screen)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(int(self.width/6), int(self.height/4)))
        # Establecer el margen inferior del texto en el botón
        back_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        back_button_border_width = int(self.height * back_button_border_width_percentage)
        back_button.setStyleSheet(f"border: {back_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        self.add_shadow_effect(back_button)   
        back_button.move(int(self.width / 1.68),int(self.height / 2))
        
        # Mostrar la ventana en pantalla completa
        self.showFullScreen()
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
        self.previous_screen = proyectoQt5.App()
        self.previous_screen.show()