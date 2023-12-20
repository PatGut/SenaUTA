from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import  QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import  QSize

import proyectoQt5 
from proyectoQt5 import dirImagenes
from screens import modulos
from screens.clases import a

width = 2040
height = 1400
colorFondo = QColor(135,206,250)

class ScreenFrases(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Frases'
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

        label = QLabel('Frases', self)
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
        container_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        container_border_width = int(self.height * container_border_width_percentage)
        container.setStyleSheet(f"border: {container_border_width}px solid #00416A; text-align: top; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container_font = QFont("Century Gothic", pointSize=int(self.height * 0.02))  # Ajusta el factor según tus necesidades
        container_font.setBold(True)  
        container.setFont(container_font)         
        container.setFixedSize(QSize(int(self.width / 2.3), int(self.height / 1.5)))
        container.move(int(self.width / 2.48), int(self.height / 5.9))
        self.add_shadow_effect(container)
        letras_button_icon = QIcon(dirImagenes+'/clase1frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2.26), int(self.height / 5.3))
        boton = QPushButton('Iniciar Clase', self)
        boton_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        boton_border_width = int(self.height * boton_border_width_percentage)
        boton.setStyleSheet(f"border: {boton_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        boton_font.setBold(True)  
        boton.setFont(boton_font)         
        boton.setFixedSize(QSize(int(self.width / 4), int(self.height / 8)))
        boton.move(int(self.width / 2), int(self.height / 1.6))
        self.add_shadow_effect(boton) 
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
        

    def class2(self):
        print('Clase 2 seleccionada')
        container = QPushButton('Clase 2', self)
        container_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        container_border_width = int(self.height * container_border_width_percentage)
        container.setStyleSheet(f"border: {container_border_width}px solid #00416A; text-align: top; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container_font = QFont("Century Gothic", pointSize=int(self.height * 0.02))  # Ajusta el factor según tus necesidades
        container_font.setBold(True)  
        container.setFont(container_font)         
        container.setFixedSize(QSize(int(self.width / 2.3), int(self.height / 1.5)))
        container.move(int(self.width / 2.48), int(self.height / 5.9))
        self.add_shadow_effect(container)
        letras_button_icon = QIcon(dirImagenes+'/clase2frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2.26), int(self.height / 5.3))
        boton = QPushButton('Iniciar Clase', self)
        boton_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        boton_border_width = int(self.height * boton_border_width_percentage)
        boton.setStyleSheet(f"border: {boton_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        boton_font.setBold(True)  
        boton.setFont(boton_font)         
        boton.setFixedSize(QSize(int(self.width / 4), int(self.height / 8)))
        boton.move(int(self.width / 2), int(self.height / 1.6))
        self.add_shadow_effect(boton) 
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class3(self):
        print('Clase 3 seleccionada')
        container = QPushButton('Clase 3', self)
        container_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        container_border_width = int(self.height * container_border_width_percentage)
        container.setStyleSheet(f"border: {container_border_width}px solid #00416A; text-align: top; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container_font = QFont("Century Gothic", pointSize=int(self.height * 0.02))  # Ajusta el factor según tus necesidades
        container_font.setBold(True)  
        container.setFont(container_font)         
        container.setFixedSize(QSize(int(self.width / 2.3), int(self.height / 1.5)))
        container.move(int(self.width / 2.48), int(self.height / 5.9))
        self.add_shadow_effect(container)
        letras_button_icon = QIcon(dirImagenes+'/clase3frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2.26), int(self.height / 5.3))
        boton = QPushButton('Iniciar Clase', self)
        boton_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        boton_border_width = int(self.height * boton_border_width_percentage)
        boton.setStyleSheet(f"border: {boton_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        boton_font.setBold(True)  
        boton.setFont(boton_font)         
        boton.setFixedSize(QSize(int(self.width / 4), int(self.height / 8)))
        boton.move(int(self.width / 2), int(self.height / 1.6))
        self.add_shadow_effect(boton) 
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class4(self):
        print('Clase 4 seleccionada')
        container = QPushButton('Clase 4', self)
        container_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        container_border_width = int(self.height * container_border_width_percentage)
        container.setStyleSheet(f"border: {container_border_width}px solid #00416A; text-align: top; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container_font = QFont("Century Gothic", pointSize=int(self.height * 0.02))  # Ajusta el factor según tus necesidades
        container_font.setBold(True)  
        container.setFont(container_font)         
        container.setFixedSize(QSize(int(self.width / 2.3), int(self.height / 1.5)))
        container.move(int(self.width / 2.48), int(self.height / 5.9))
        self.add_shadow_effect(container)
        letras_button_icon = QIcon(dirImagenes+'/clase4frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(int(self.width / 2.84), int(self.height / 2)))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2.26), int(self.height / 5.3))
        boton = QPushButton('Iniciar Clase', self)
        boton_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        boton_border_width = int(self.height * boton_border_width_percentage)
        boton.setStyleSheet(f"border: {boton_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        boton_font.setBold(True)  
        boton.setFont(boton_font)         
        boton.setFixedSize(QSize(int(self.width / 4), int(self.height / 8)))
        boton.move(int(self.width / 2), int(self.height / 1.6))
        self.add_shadow_effect(boton) 
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
    


    def iniciarClase(self):
        print('Clase iniciada')
        self.next_screen = a.ScreenRealizarClase()
        self.next_screen.show()
        self.hide()

    def show_next_screen(self):
        self.next_screen = proyectoQt5.App()
        self.next_screen.show()
        self.hide()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = modulos.ScreenModulos()
        self.previous_screen.show()