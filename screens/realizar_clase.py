from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect, QTimer
from PyQt5.QtMultimedia import QCamera
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

import prueba_pyqt5 
from screens import modulos, abc


width = 2040
height = 1400
dirImagenes = 'C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes'
colorFondo = QColor(135,206,250)

class ScreenRealizarClase(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Realizar Clase'
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

        label = QLabel('Realizando Clase', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-weight: bold; font-size: 100px;  color: #00416A;")
        container = QPushButton('A', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(800, 700))
        container.move(int(self.width / 3) - 600, 270) 
        imagen = QLabel(self)
        pixmap = QPixmap(dirImagenes+'/letraA.png')
        imagen.setPixmap(pixmap)
        imagen.setFixedSize(pixmap.width(), pixmap.height())
        # Mover la imagen a la posición central
        imagen.move(int(container.width()/2)-150, int(container.height()/2)+50)

        camaraContainer = QPushButton('',self)
        camaraContainer.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        camaraContainer.setFixedSize(QSize(950, 800))
        camaraContainer.move(int(self.width / 2) -50, 270) 
        # Crea una instancia de QCamera y QCameraViewfinder
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(camaraContainer.size())
        self.viewfinder.move(int(self.width / 2) - 50, 270)
        #1920 x 1080
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(500, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(300, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px;  border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 3) - int(back_button.width()),1150)

        boton = QPushButton('Siguiente', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 400, 1150)
        boton.clicked.connect(self.to_next_screen)

        self.show()

    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = modulos.ScreenModulos()
        self.previous_screen.show()

    def to_next_screen(self):
        self.camera.stop()
        self.hide()
        self.next_screen = ScreenB()
        self.next_screen.show()

class ScreenB(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Realizar Clase'
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

        label = QLabel('Realizando Clase', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-weight: bold; font-size: 100px;  color: #00416A;")
        container = QPushButton('B', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(800, 700))
        container.move(int(self.width / 3) - 600, 270) 
        #imagen = QLabel(self)
        #pixmap = QPixmap(dirImagenes+'/letraA.png')
        #imagen.setPixmap(pixmap)
        #imagen.setFixedSize(pixmap.width(), pixmap.height())
        # Mover la imagen a la posición central
        #imagen.move(int(container.width()/2)-150, int(container.height()/2)+50)

        camaraContainer = QPushButton('',self)
        camaraContainer.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        camaraContainer.setFixedSize(QSize(950, 800))
        camaraContainer.move(int(self.width / 2) -50, 270) 
        # Crea una instancia de QCamera y QCameraViewfinder
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(camaraContainer.size())
        self.viewfinder.move(int(self.width / 2) - 50, 270)
        #1920 x 1080
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(500, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(300, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px;  border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 3) - int(back_button.width()),1150)

        boton = QPushButton('Siguiente', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 400, 1150)
        boton.clicked.connect(self.to_next_screen)


        self.show()

    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = ScreenRealizarClase()
        self.previous_screen.show()

    def to_next_screen(self):
        self.camera.stop()
        self.hide()
        self.next_screen = ScreenC()
        self.next_screen.show()

class ScreenC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Realizar Clase'
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

        label = QLabel('Realizando Clase', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-weight: bold; font-size: 100px;  color: #00416A;")
        container = QPushButton('C', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(800, 700))
        container.move(int(self.width / 3) - 600, 270) 
        #imagen = QLabel(self)
        #pixmap = QPixmap(dirImagenes+'/letraA.png')
        #imagen.setPixmap(pixmap)
        #imagen.setFixedSize(pixmap.width(), pixmap.height())
        # Mover la imagen a la posición central
        #imagen.move(int(container.width()/2)-150, int(container.height()/2)+50)

        camaraContainer = QPushButton('',self)
        camaraContainer.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        camaraContainer.setFixedSize(QSize(950, 800))
        camaraContainer.move(int(self.width / 2) -50, 270) 
        # Crea una instancia de QCamera y QCameraViewfinder
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(camaraContainer.size())
        self.viewfinder.move(int(self.width / 2) - 50, 270)
        #1920 x 1080
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(500, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(300, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px;  border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 3) - int(back_button.width()),1150)

        boton = QPushButton('Siguiente', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 400, 1150)
        boton.clicked.connect(self.to_next_screen)


        self.show()

    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = ScreenB()
        self.previous_screen.show()

    def to_next_screen(self):
        self.camera.stop()
        self.hide()
        self.next_screen = ScreenD()
        self.next_screen.show()

class ScreenD(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Realizar Clase'
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

        label = QLabel('Realizando Clase', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-weight: bold; font-size: 100px;  color: #00416A;")
        container = QPushButton('D', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(800, 700))
        container.move(int(self.width / 3) - 600, 270) 
        #imagen = QLabel(self)
        #pixmap = QPixmap(dirImagenes+'/letraA.png')
        #imagen.setPixmap(pixmap)
        #imagen.setFixedSize(pixmap.width(), pixmap.height())
        # Mover la imagen a la posición central
        #imagen.move(int(container.width()/2)-150, int(container.height()/2)+50)

        camaraContainer = QPushButton('',self)
        camaraContainer.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        camaraContainer.setFixedSize(QSize(950, 800))
        camaraContainer.move(int(self.width / 2) -50, 270) 
        # Crea una instancia de QCamera y QCameraViewfinder
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(camaraContainer.size())
        self.viewfinder.move(int(self.width / 2) - 50, 270)
        #1920 x 1080
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(500, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(300, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px;  border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 3) - int(back_button.width()),1150)

        boton = QPushButton('Siguiente', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 400, 1150)
        boton.clicked.connect(self.to_next_screen)


        self.show()

    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = ScreenC()
        self.previous_screen.show()

    def to_next_screen(self):
        self.camera.stop()
        self.hide()
        self.next_screen = ScreenE()
        self.next_screen.show()

class ScreenE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Realizar Clase'
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

        label = QLabel('Realizando Clase', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-weight: bold; font-size: 100px;  color: #00416A;")
        container = QPushButton('E', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        container.setFixedSize(QSize(800, 700))
        container.move(int(self.width / 3) - 600, 270) 
        #imagen = QLabel(self)
        #pixmap = QPixmap(dirImagenes+'/letraA.png')
        #imagen.setPixmap(pixmap)
        #imagen.setFixedSize(pixmap.width(), pixmap.height())
        # Mover la imagen a la posición central
        #imagen.move(int(container.width()/2)-150, int(container.height()/2)+50)

        camaraContainer = QPushButton('',self)
        camaraContainer.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: 10px solid #00416A; border-radius: 50px; padding: 50px; background-color: #BFF5F5; color: #00416A; ")
        camaraContainer.setFixedSize(QSize(950, 800))
        camaraContainer.move(int(self.width / 2) -50, 270) 
        # Crea una instancia de QCamera y QCameraViewfinder
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder(self)
        self.viewfinder.setFixedSize(camaraContainer.size())
        self.viewfinder.move(int(self.width / 2) - 50, 270)
        #1920 x 1080
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(500, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(300, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px;  border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 3) - int(back_button.width()),1150)

        boton = QPushButton('Finalizar', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; font-weight: bold; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 400, 1150)
        boton.clicked.connect(self.to_next_screen)


        self.show()

    def back_to_previous_screen(self):
        self.camera.stop()
        self.hide()
        self.previous_screen = ScreenD()
        self.previous_screen.show()

    def to_next_screen(self):
        self.camera.stop()
        self.hide()
        self.next_screen = abc.ScreenABC()
        self.next_screen.show()