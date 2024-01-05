import argparse
from PyQt5.QtWidgets import  QMainWindow, QPushButton, QLabel,  QDesktopWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import  QPixmap, QPalette, QColor, QFont, QIcon, QMovie
from PyQt5.QtCore import  QSize
from senaUtaEduca import dirImagenes
from utils import video
from screens.clases import n, o
colorFondo = QColor(135,206,250)
class ScreenÑ(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Realizar Clase'
        self.width, self.height = self.get_screen_resolution()

        self.initUI()

#Funcion para obtener la resolución de la pantalla
    def get_screen_resolution(self):
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        return screen_rect.width(), screen_rect.height()
#Funcion para sombreado de botones
    def add_shadow_effect(self, widget):
        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(10, 10)
        widget.setGraphicsEffect(shadow)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana
        palette = QPalette()
        palette.setColor(QPalette.Window, colorFondo)
        self.setPalette(palette)

        label = QLabel('REALIZANDO CLASE', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))
        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-weight: bold; font-size: 100px;  color: #00416A;")
        container = QPushButton('Ñ', self)
        container_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        container_border_width = int(self.height * container_border_width_percentage)
        container.setStyleSheet(f"border: {container_border_width}px solid #00416A; text-align: top; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container_font = QFont("Calibri", pointSize=int(self.height * 0.02))  # Ajusta el factor según tus necesidades
        container_font.setBold(True)  
        container.setFont(container_font)         
        container.setFixedSize(QSize(int(self.width / 3.2), int(self.height / 2.28)))
        container.move(int(self.width / 10.11), int(self.height / 5.9))
        self.add_shadow_effect(container) 
        imagen = QLabel(self)
        pixmap = QPixmap(dirImagenes+'/letraÑ.png')
        imagen.setPixmap(pixmap)
        imagen.setFixedSize(pixmap.width(), pixmap.height())
        # Mover la imagen a la posición central
        imagen.move(int(container.width()/2.5), int(container.height()/1.75))

        camaraContainer = QPushButton('',self)
        camaraContainer_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        camaraContainer_border_width = int(self.height * camaraContainer_border_width_percentage)    
        camaraContainer.setFixedSize(QSize(int(self.width / 2.69), int(self.height / 2)))
        camaraContainer.setStyleSheet(f"border: {camaraContainer_border_width}px solid #00416A;font-family: Century Gothic;  font-weight: bold;font-size: 50px; text-align: top; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        camaraContainer.move(int(self.width / 2.08), int(self.height / 5.92)) 
        self.add_shadow_effect(camaraContainer) 

        # Imagen Gif
        labelCargando = QLabel(self)
        # Crea el QMovie y asigna el archivo GIF
        self.movie = QMovie(dirImagenes+'/load.gif')
        # Asigna el QMovie al QLabel
        labelCargando.setMovie(self.movie)
        # Inicia la animación del GIF
        self.movie.start()
        # Ajusta el tamaño del QLabel al tamaño del GIF
        labelCargando.setFixedSize(QSize(int(self.width / 2.69), int(self.height / 2)))
        # Mover la imagen a la posición central
        labelCargando.move(int(self.width / 1.75),int(self.height / 6))


        #Hilos
        # Inicializar QLabel para mostrar el video
        self.image_label = QLabel(self)
        self.image_label.resize(QSize(int(self.width / 2.8), int(self.height / 2.2)))  # Ajusta el tamaño según tus necesidades
        self.image_label.move(int(self.width / 2.05),int(self.height / 5.2))  # Ajusta la posición según tus necesidades
    
        args = ScreenÑ.get_args()  # Asegúrate de que esta función devuelva los argumentos necesarios
        self.thread = video.VideoThread(args)
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(int(self.width / 5.12), int(self.height / 7)))        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(int(self.width / 8), int(self.height / 7)))
        # Establecer el margen inferior del texto en el botón
        back_button_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        back_button_border_width = int(self.height * back_button_border_width_percentage)
        back_button.setStyleSheet(f"border: {back_button_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        back_button.move(int(self.width / 7.3),int(self.height / 1.39))
        back_button.clicked.connect(self.back_to_previous_screen)
        self.add_shadow_effect(back_button)


        boton = QPushButton('Siguiente', self)
        boton_border_width_percentage = 0.009  # Ajusta el porcentaje según tus necesidades
        boton_border_width = int(self.height * boton_border_width_percentage)
        boton.setStyleSheet(f"border: {boton_border_width}px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton_font = QFont("Century Gothic", pointSize=int(self.height * 0.018))  # Ajusta el factor según tus necesidades
        boton_font.setBold(True) 
        boton.setFont(boton_font)         
        boton.setFixedSize(QSize(int(self.width / 5.12), int(self.height / 8)))
        boton.move(int(self.width / 1.52), int(self.height / 1.39))
        boton.clicked.connect(self.to_next_screen)
        self.add_shadow_effect(boton)

        self.showFullScreen()
        self.show()

    #Funciones para actualizar la imagen y obtener datos
    def update_image(self, cv_img):
        qt_img = QPixmap.fromImage(cv_img)
        self.image_label.setPixmap(qt_img)  # Asegúrate de que image_label está definido
    
    
    def get_args():
        parser = argparse.ArgumentParser()

        parser.add_argument("--device", type=int, default=0)
        parser.add_argument("--width", help='cap width', type=int, default=960)
        parser.add_argument("--height", help='cap height', type=int, default=540)

        parser.add_argument('--use_static_image_mode', action='store_false')
        parser.add_argument("--min_detection_confidence",
                            help='min_detection_confidence',
                            type=float,
                            default=0.7)
        parser.add_argument("--min_tracking_confidence",
                            help='min_tracking_confidence',
                            type=int,
                            default=0.5)
        parser.add_argument("--letra", type=str, default="Ñ")
        args = parser.parse_args()
        return args

    def back_to_previous_screen(self):
        # Detener el thread de video
        if self.thread.isRunning():
            self.thread.stop()
        
        self.previous_screen = n.ScreenN()
        self.previous_screen.show()
        self.hide()

    def to_next_screen(self):
        # Detener el thread de video
        if self.thread.isRunning():
            self.thread.stop()
        
        self.next_screen = o.ScreenO()
        self.next_screen.show()
        self.hide()