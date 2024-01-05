from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QDesktopWidget, QGraphicsDropShadowEffect,  QGridLayout, QWidget
from PyQt5.QtGui import  QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import  QSize

import senaUtaEduca 
from senaUtaEduca import dirImagenes
from screens import modulos, practica

colorFondo = QColor(135,206,250)

class ScreenFrases(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Frases'
        self.width, self.height = self.get_screen_resolution()
        self.active_containers = []
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
    #Función para ocultar container anterior
    def hide_previous_containers(self):
        for container in self.active_containers:
            container.hide()  # Oculta el contenedor
            container.deleteLater()  # Elimina el contenedor
        self.active_containers.clear()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana
        palette = QPalette()
        palette.setColor(QPalette.Window, colorFondo)
        self.setPalette(palette)
        # Crear un layout de cuadrícula
        grid_layout = QGridLayout()

        label = QLabel('FRASES', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(900, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;font-weight: bold;    color: #00416A;")
        grid_layout.addWidget(label, 0, 0, 1, 2)  # Agregar la etiqueta a la cuadrícula

        #CLASE 1
        clase1_button = QPushButton('Clase 1', self)
        clase1_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        clase1_button_border_width = int(self.height * clase1_button_border_width_percentage)
        clase1_button.setStyleSheet(f"border: {clase1_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase1_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        clase1_button_font.setBold(True) 
        clase1_button.setFont(clase1_button_font) 
        clase1_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        clase1_button.clicked.connect(self.class1)
        self.add_shadow_effect(clase1_button)   
        grid_layout.addWidget(clase1_button, 1, 0)  # Agregar el botón a la cuadrícula


        #CLASE 2
        clase2_button = QPushButton('Clase 2', self)
        clase2_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        clase2_button_border_width = int(self.height * clase2_button_border_width_percentage)
        clase2_button.setStyleSheet(f"border: {clase2_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase2_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        clase2_button_font.setBold(True) 
        clase2_button.setFont(clase2_button_font) 
        clase2_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        clase2_button.clicked.connect(self.class2)    
        self.add_shadow_effect(clase2_button)   
        grid_layout.addWidget(clase2_button, 2, 0)  # Agregar el botón a la cuadrícula

        #CLASE 3
        clase3_button = QPushButton('Clase 3', self)
        clase3_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        clase3_button_border_width = int(self.height * clase3_button_border_width_percentage)
        clase3_button.setStyleSheet(f"border: {clase3_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase3_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        clase3_button_font.setBold(True) 
        clase3_button.setFont(clase3_button_font) 
        clase3_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        clase3_button.clicked.connect(self.class3)    
        self.add_shadow_effect(clase3_button)   
        grid_layout.addWidget(clase3_button, 3, 0)  # Agregar el botón a la cuadrícula

        #CLASE 4
        clase4_button = QPushButton('Clase 4', self)
        clase4_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        clase4_button_border_width = int(self.height * clase4_button_border_width_percentage)
        clase4_button.setStyleSheet(f"border: {clase4_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase4_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        clase4_button_font.setBold(True) 
        clase4_button.setFont(clase4_button_font) 
        clase4_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        clase4_button.clicked.connect(self.class4)
        self.add_shadow_effect(clase4_button)   
        grid_layout.addWidget(clase4_button, 4, 0)  # Agregar el botón a la cuadrícula   



       # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')  # Asegúrate de que el nombre del ícono sea correcto
        back_button = QPushButton('', self)
        back_button_border_width_percentage = 0.009
        back_button_border_width = int(self.height * back_button_border_width_percentage)
        back_button.setStyleSheet(f"border: {back_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        back_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))
        back_button_font.setBold(True) 
        back_button.setFont(back_button_font) 
        back_button.setFixedSize(QSize(int(self.width/12), int(self.height/7)))
        back_button.setIcon(back_button_icon)
        # Establecer el ícono directamente en el botón
        back_button.setIcon(back_button_icon)
        back_button.setIconSize(QSize(int(self.width/12), int(self.height/7)))
        back_button.clicked.connect(self.back_to_previous_screen)
        self.add_shadow_effect(back_button)   
        grid_layout.addWidget(back_button, 0, 3)
        
        # Establecer el layout de la ventana
        central_widget = QWidget(self)
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)
        
        # Mostrar la ventana en pantalla completa
        self.showFullScreen()
        self.show()

    def class1(self):
        print('Clase 1 seleccionada')
        container = QPushButton('CLASE 1', self)
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
        container = QPushButton('CLASE 2', self)
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
        container = QPushButton('CLASE 3', self)
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
        container = QPushButton('CLASE 4', self)
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
        self.next_screen = practica.ScreenPractica()
        self.next_screen.show()
        self.hide()

    def show_next_screen(self):
        self.next_screen = senaUtaEduca.App()
        self.next_screen.show()
        self.hide()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = modulos.ScreenModulos()
        self.previous_screen.show()