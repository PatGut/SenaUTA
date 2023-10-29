
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Inicio'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)        
        self.setGeometry(QApplication.desktop().screenGeometry())

        # Cambiar el color de fondo a #F3E5AB
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)
        # Imagen con url
        label = QLabel(self)
        pixmap = QPixmap('C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes/SeñaUta.png')
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())
        # Calcular la posición central
        center_x = int((self.width() - pixmap.width()) / 2)
        center_y = int((self.height() - pixmap.height()) / 2 - 400)
        # Mover la imagen a la posición central
        label.move(center_x, center_y)

        # Botón para cambiar a la siguiente pantalla
        clases_button = QPushButton('Clases', self)
        clases_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black; ")
        clases_button.setFixedSize(QSize(500, 200))
        clases_button.move(int(self.width() / 2) - int(clases_button.width() / 2), int(self.height() / 2) - int(clases_button.height()))
        clases_button.clicked.connect(self.show_next_screen)

        # Botón para cambiar a la pantalla de prueba
        prueba_button = QPushButton('Prueba', self)
        prueba_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black; ")
        prueba_button.setFixedSize(QSize(500, 200))
        print(int(self.height() / 2) + int(prueba_button.height()) + 20)
        prueba_button.move(int(self.width() / 2) - int(prueba_button.width() / 2), int(self.height() / 2) + 20)
        prueba_button.clicked.connect(self.show_prueba_screen)

        # Botón para salir del programa
        exit_button = QPushButton('Salir', self)
        exit_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black;")
        exit_button.setFixedSize(QSize(500, 200))
        exit_button.move(int(self.width() / 2) - int(exit_button.width() / 2), int(self.height() / 2) + int(prueba_button.height()) + 40)
        exit_button.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    def show_next_screen(self):
        self.next_screen = ScreenModulos()
        self.next_screen.show()
        self.hide()

    def show_prueba_screen(self):
        self.next_screen = ScreenPractica()
        self.next_screen.show()
        self.hide()

class ScreenPractica(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Práctica Libre'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(QApplication.desktop().screenGeometry())
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)
        self.menuBar().setNativeMenuBar(False)
    # Botón 'Volver'
        back_button = QPushButton('Volver', self)
        back_button.setFixedSize(QSize(500, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width() / 2) - int(back_button.width() / 2),1000)

        self.show()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = App()
        self.previous_screen.show()

    
class ScreenModulos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Módulos'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(QApplication.desktop().screenGeometry())
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)

        # Agregar la etiqueta 'modulos' al layout
        label = QLabel('Módulos', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(500, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;  color: black;")

        # Cargar la imagen
        self.button_icon = QIcon('C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes/uta_vertical.png')

        # Crear el botón y establecer la etiqueta
        self_button = QPushButton('Clase 1', self)
        self_button.setFixedSize(QSize(500, 200))
        self_button.setIcon(self.button_icon)
        self_button.setText('Clase 1')
        self_button.clicked.connect(self.class1)
        # Establecer el tamaño del icono
        self_button.setIconSize(QSize(160, 160))
        # Establecer el margen inferior del texto en el botón
        self_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding-right: 50px; background-color: #F0DE9A; color: black; ")

        self_button.move(int(self.width() / 2) - int(self_button.width() / 2),400)

        # Botón 'clase 2'
        button2 = QPushButton('Clase 2', self)
        button2.setFixedSize(QSize(500, 200))
        button2.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black; ")

        button2.clicked.connect(self.class2)
        button2.move(int(self.width() / 2) - int(self_button.width() / 2),700)

        # Botón 'Volver'
        back_button = QPushButton('Volver', self)
        back_button.setFixedSize(QSize(500, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width() / 2) - int(self_button.width() / 2),1000)

        self.show()

    def class1(self):
        print('Clase 1 seleccionada')

    def class2(self):
        print('Clase 2 seleccionada')

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = App()
        self.previous_screen.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())