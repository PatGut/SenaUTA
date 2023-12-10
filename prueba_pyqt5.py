from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout, QDesktopWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import sys
import os
from screens import modulos
from screens import practica

dirImagenes = os.path.join(os.path.dirname(__file__), 'Imagenes')
colorFondo = QColor(135,206,250)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Inicio'
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

        # Cambiar el color de fondo a #F3E5AB
        palette = QPalette()
        palette.setColor(QPalette.Window, colorFondo)
        self.setPalette(palette)

        # Crear un layout vertical
        vertical_layout = QVBoxLayout()

        # Imagen con url
        label = QLabel(self)
        pixmap = QPixmap(dirImagenes+'/SeñaUta.png')
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())
        
        # Calcular la posición central
        center_x = int((self.width - pixmap.width()) / 2)
        center_y = int((self.height - pixmap.height()) / 2)
        
        # Mover la imagen a la posición central
        label.move(center_x, center_y)
        vertical_layout.addWidget(label, alignment=Qt.AlignCenter)  # Agregar la etiqueta al layout

        # Botón para cambiar a la siguiente pantalla
        clases_button = QPushButton('Clases', self)
        border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        border_width = int(self.height * border_width_percentage)
        clases_button.setStyleSheet(f"border: {border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clases_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        clases_button_font.setBold(True) 
        clases_button.setFont(clases_button_font)        
        clases_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        vertical_layout.addWidget(clases_button, alignment=Qt.AlignCenter)  # Agregar el botón al layout
        clases_button.clicked.connect(self.show_next_screen)
        self.add_shadow_effect(clases_button)

        # Botón para cambiar a la pantalla de prueba
        prueba_button = QPushButton('Prueba', self)
        prueba_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        prueba_button_border_width = int(self.height * prueba_button_border_width_percentage)
        prueba_button.setStyleSheet(f"border: {prueba_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        prueba_button_font = QFont("Century Gothic", pointSize= int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        prueba_button_font.setBold(True) 
        prueba_button.setFont(prueba_button_font)
        prueba_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))
        vertical_layout.addWidget(prueba_button, alignment=Qt.AlignCenter)  # Agregar el botón al layout
        prueba_button.clicked.connect(self.show_prueba_screen)
        self.add_shadow_effect(prueba_button)


        # Botón para salir del programa
        exit_button = QPushButton('Salir', self)
        exit_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        exit_button_border_width = int(self.height * exit_button_border_width_percentage)
        exit_button.setStyleSheet(f"border: {exit_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        exit_button_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        exit_button_font.setBold(True) 
        exit_button.setFont(exit_button_font)
        exit_button.setFixedSize(QSize(int(self.width/4), int(self.height/7)))        
        vertical_layout.addWidget(exit_button, alignment=Qt.AlignCenter)  # Agregar el botón al layout
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        self.add_shadow_effect(exit_button)
        
        # Establecer el layout de la ventana
        central_widget = QWidget(self)
        central_widget.setLayout(vertical_layout)
        self.setCentralWidget(central_widget)
        
        # Mostrar la ventana en pantalla completa
        self.showFullScreen()
        self.show()

    #Cambiar a la pantalla Módulos
    def show_next_screen(self):
        self.next_screen = modulos.ScreenModulos()
        self.next_screen.show()
        self.hide()
        
    #Cambiar a la pantalla Práctica
    def show_prueba_screen(self):
        self.next_screen = practica.ScreenPractica()
        self.next_screen.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())