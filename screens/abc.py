from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDesktopWidget, QGraphicsDropShadowEffect, QGridLayout
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

import prueba_pyqt5 
from prueba_pyqt5 import dirImagenes
from screens import modulos
from screens import realizar_clase


colorFondo = QColor(135,206,250)

class ScreenABC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Abecedario'
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

        # Crear un layout de cuadrícula
        grid_layout = QGridLayout()

        label = QLabel('ABECEDARIO', self)
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

        #CLASE 5
        clase5_button = QPushButton('Clase 5', self)
        clase5_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        clase5_button_border_width = int(self.height * clase5_button_border_width_percentage)
        clase5_button.setStyleSheet(f"border: {clase5_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clase5_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        clase5_button_font.setBold(True) 
        clase5_button.setFont(clase5_button_font) 
        clase5_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        clase5_button.clicked.connect(self.class5) 
        self.add_shadow_effect(clase5_button)   
        grid_layout.addWidget(clase5_button, 5, 0)  # Agregar el botón a la cuadrícula 
       


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
        container = QPushButton('Clase 1', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase1abc.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A;  border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
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
        letras_button_icon = QIcon(dirImagenes+'/clase2abc.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
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
        letras_button_icon = QIcon(dirImagenes+'/clase3abc.png')
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
        letras_button_icon = QIcon(dirImagenes+'/clase4abc.png')
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
    
    def class5(self):
        print('Clase 5 seleccionada')
        container = QPushButton('Clase 5', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase5abc.png')
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