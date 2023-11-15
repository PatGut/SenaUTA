
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt, QCoreApplication, QSize, QRect
import sys
width = 2040
height = 1400
dirImagenes = 'C:/Users/katia/OneDrive/Documentos/Proyecto 4/SenaUTA/Imagenes'
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Inicio'
        self.width = width
        self.height = height  # Define las dimensiones deseadas
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)        
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana


        # Cambiar el color de fondo a #F3E5AB
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(135,206,250))
        self.setPalette(palette)
        # Imagen con url
        label = QLabel(self)
        pixmap = QPixmap(dirImagenes+'/SeñaUta.png')
        label.setPixmap(pixmap)
        label.setFixedSize(pixmap.width(), pixmap.height())
        # Calcular la posición central
        center_x = int((self.width - pixmap.width()) / 2)
        center_y = int((self.height - pixmap.height()) / 2 - 400)
        # Mover la imagen a la posición central
        label.move(center_x, center_y)

        # Botón para cambiar a la siguiente pantalla
        clases_button = QPushButton('Clases', self)
        clases_button.setStyleSheet("font-family: Century Gothic;  font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        clases_button.setFixedSize(QSize(500, 200))
        clases_button.move(int(self.width / 2) - int(clases_button.width() / 2), int(self.height / 2) - int(clases_button.height()))
        clases_button.clicked.connect(self.show_next_screen)

        # Botón para cambiar a la pantalla de prueba
        prueba_button = QPushButton('Prueba', self)
        prueba_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A; ")
        prueba_button.setFixedSize(QSize(500, 200))
        print(int(self.height / 2) + int(prueba_button.height()) + 20)
        prueba_button.move(int(self.width / 2) - int(prueba_button.width() / 2), int(self.height / 2) + 20)
        prueba_button.clicked.connect(self.show_prueba_screen)

        # Botón para salir del programa
        #exit_button_icon = QIcon()#dirImagenes+'/salir.png'
        exit_button = QPushButton('Salir', self)
        exit_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #BFF5F5; color: #00416A;")
        exit_button.setFixedSize(QSize(500, 200))        
        #exit_button.setIcon(exit_button_icon)
        # Establecer el tamaño del icono
        #exit_button.setIconSize(QSize(160, 160))
        exit_button.move(int(self.width / 2) - int(exit_button.width() / 2), int(self.height / 2) + int(prueba_button.height()) + 40)
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
        self.width = width
        self.height = height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)
        self.menuBar().setNativeMenuBar(False)
    # Botón 'Volver'
        back_button = QPushButton('Volver', self)
        back_button.setFixedSize(QSize(500, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) - int(back_button.width() / 2),1000)

        self.show()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = App()
        self.previous_screen.show()

    
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
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
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
        self_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; background-color: #F0DE9A; color: #00416A; ")

        self_button.move(int(self.width / 3) - int(self_button.width()) + 250,230)

        # Botón 'clase 2'
        button2_icon = QIcon(dirImagenes+'/palabras.png')
        button2 = QPushButton(self)
        button2.setFixedSize(QSize(750, 500))
        button2.setIcon(button2_icon)
        # Establecer el tamaño del icono
        button2.setIconSize(QSize(650, 400))
        button2.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        button2.clicked.connect(self.class2)
        button2.move(int(self.width / 2) - int(self_button.width() / 2)+ 250,230)

        # Botón 'clase 3'
        button3_icon = QIcon(dirImagenes+'/frases.png')
        button3 = QPushButton(self)
        button3.setFixedSize(QSize(960, 500))
        button3.setIcon(button3_icon)
        # Establecer el tamaño del icono
        button3.setIconSize(QSize(800, 500))
        button3.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        button3.clicked.connect(self.class3)
        button3.move(int(self.width / 3) - int(self_button.width()) + 250,770)

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(400, 500))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(400, 400))
        back_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: black; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) + int(button3.width()/2) - 170,770)

        self.show()

    def class1(self):
        print('Módulo ABC seleccionado')
        self.next_screen = ScreenABC()
        self.next_screen.show()
        self.hide()

    def class2(self):
        print('Módulo Palabras seleccionado')
        self.next_screen = ScreenPalabras()
        self.next_screen.show()
        self.hide()
    
    def class3(self):
        print('Módulo Frases seleccionado')
        self.next_screen = ScreenFrases()
        self.next_screen.show()
        self.hide()

        

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = App()
        self.previous_screen.show()

class ScreenABC(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Abecedario'
        self.width = width
        self.height = height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)  # Establece las dimensiones
        self.setFixedSize(self.size())  # Bloquea el cambio de tamaño de la ventana
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)

        label = QLabel('Abecedario', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(900, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;font-weight: bold;    color: #00416A;")

        clase1_button = QPushButton('Clase 1', self)
        clase1_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase1_button.setFixedSize(QSize(500, 200))
        clase1_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 230)
        clase1_button.clicked.connect(self.class1)    

        clase2_button = QPushButton('Clase 2', self)
        clase2_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase2_button.setFixedSize(QSize(500, 200))
        clase2_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 450)
        clase2_button.clicked.connect(self.class2)    

        clase3_button = QPushButton('Clase 3', self)
        clase3_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase3_button.setFixedSize(QSize(500, 200))
        clase3_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 670)
        clase3_button.clicked.connect(self.class3)    

        clase4_button = QPushButton('Clase 4', self)
        clase4_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase4_button.setFixedSize(QSize(500, 200))
        clase4_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 890)
        clase4_button.clicked.connect(self.class4)    

        clase5_button = QPushButton('Clase 5', self)
        clase5_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
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
        back_button.setStyleSheet("font-family: Century Gothic; font-weight: bold; font-size: 60px; border: 10px solid #00416A; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) + int(back_button.width()) + 600 ,30)

        self.show()

    def class1(self):
        print('Clase 1 seleccionada')
        container = QPushButton('Clase 1', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
        

    def class2(self):
        print('Clase 2 seleccionada')
        container = QPushButton('Clase 2', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class3(self):
        print('Clase 3 seleccionada')
        container = QPushButton('Clase 3', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class4(self):
        print('Clase 4 seleccionada')
        container = QPushButton('Clase 4', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
    
    def class5(self):
        print('Clase 5 seleccionada')
        container = QPushButton('Clase 5', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def iniciarClase(self):
        print('Clase iniciada')
        self.next_screen = ScreenRealizarClase()
        self.next_screen.show()
        self.hide()

    def show_next_screen(self):
        self.next_screen = App()
        self.next_screen.show()
        self.hide()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = ScreenModulos()
        self.previous_screen.show()

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
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)

        label = QLabel('Palabras', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(900, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;  color: #00416A;")

        clase1_button = QPushButton('Clase 1', self)
        clase1_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase1_button.setFixedSize(QSize(500, 200))
        clase1_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 230)
        clase1_button.clicked.connect(self.class1)    

        clase2_button = QPushButton('Clase 2', self)
        clase2_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase2_button.setFixedSize(QSize(500, 200))
        clase2_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 450)
        clase2_button.clicked.connect(self.class2)    

        clase3_button = QPushButton('Clase 3', self)
        clase3_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase3_button.setFixedSize(QSize(500, 200))
        clase3_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 670)
        clase3_button.clicked.connect(self.class3)    

        clase4_button = QPushButton('Clase 4', self)
        clase4_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase4_button.setFixedSize(QSize(500, 200))
        clase4_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 890)
        clase4_button.clicked.connect(self.class4)    

        clase5_button = QPushButton('Clase 5', self)
        clase5_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
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
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) + int(back_button.width()) + 600 ,30)

        self.show()

    def class1(self):
        print('Clase 1 seleccionada')
        container = QPushButton('Clase 1', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
        

    def class2(self):
        print('Clase 2 seleccionada')
        container = QPushButton('Clase 2', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class3(self):
        print('Clase 3 seleccionada')
        container = QPushButton('Clase 3', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class4(self):
        print('Clase 4 seleccionada')
        container = QPushButton('Clase 4', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
    
    def class5(self):
        print('Clase 5 seleccionada')
        container = QPushButton('Clase 5', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
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
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def iniciarClase(self):
        print('Clase iniciada')
        self.next_screen = ScreenRealizarClase()
        self.next_screen.show()
        self.hide()

    def show_next_screen(self):
        self.next_screen = App()
        self.next_screen.show()
        self.hide()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = ScreenModulos()
        self.previous_screen.show()

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
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)

        label = QLabel('Frases', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(900, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;  color: #00416A;")

        clase1_button = QPushButton('Clase 1', self)
        clase1_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase1_button.setFixedSize(QSize(500, 200))
        clase1_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 230)
        clase1_button.clicked.connect(self.class1)    

        clase2_button = QPushButton('Clase 2', self)
        clase2_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase2_button.setFixedSize(QSize(500, 200))
        clase2_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 450)
        clase2_button.clicked.connect(self.class2)    

        clase3_button = QPushButton('Clase 3', self)
        clase3_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        clase3_button.setFixedSize(QSize(500, 200))
        clase3_button.move(int(self.width / 3) - int(clase1_button.width())  - 100, 670)
        clase3_button.clicked.connect(self.class3)    

        clase4_button = QPushButton('Clase 4', self)
        clase4_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
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
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 2) + int(back_button.width()) + 600 ,30)

        self.show()

    def class1(self):
        print('Clase 1 seleccionada')
        container = QPushButton('Clase 1', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase1frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
        

    def class2(self):
        print('Clase 2 seleccionada')
        container = QPushButton('Clase 2', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase2frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class3(self):
        print('Clase 3 seleccionada')
        container = QPushButton('Clase 3', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase3frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()

    def class4(self):
        print('Clase 4 seleccionada')
        container = QPushButton('Clase 4', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
        container.setFixedSize(QSize(1100, 1000))
        container.move(int(self.width / 2) - int(500/2), 270)
        letras_button_icon = QIcon(dirImagenes+'/clase4frases.png')
        letras_button = QPushButton(self)
        letras_button.setFixedSize(QSize(900, 800))
        letras_button.setIcon(letras_button_icon)
        letras_button.setIconSize(QSize(900, 800))
        letras_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; color: #00416A; ")
        letras_button.move(int(self.width / 2) - int(500/2)+100, 300)
        boton = QPushButton('Iniciar Clase', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 280, 1000)
        boton.clicked.connect(self.iniciarClase) 
        container.show()
        letras_button.show()
        boton.show()
    


    def iniciarClase(self):
        print('Clase iniciada')
        self.next_screen = ScreenRealizarClase()
        self.next_screen.show()
        self.hide()

    def show_next_screen(self):
        self.next_screen = App()
        self.next_screen.show()
        self.hide()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = ScreenModulos()
        self.previous_screen.show()

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
        palette.setColor(QPalette.Window, QColor(246, 237, 198))
        self.setPalette(palette)

        label = QLabel('Realizando Clase', self)
        label.setFont(label.font())
        label.setFixedSize(QSize(1000, 200))

        label.setStyleSheet("font-family: Century Gothic; padding-left: 50px; font-size: 100px;  color: #00416A;")
        container = QPushButton('A', self)
        container.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #F4C374; color: #00416A; ")
        container.setFixedSize(QSize(800, 700))
        container.move(int(self.width / 3) - 600, 270) 

        camara = QPushButton('Activar cámara',self)
        camara.setStyleSheet("text-align: top; font-family: Century Gothic;  font-weight: bold; font-size: 50px; border: none; border-radius: 50px; padding: 50px; background-color: #CBB187; color: #00416A; ")
        camara.setFixedSize(QSize(950, 800))
        camara.move(int(self.width / 2) -50, 270) 

        # Botón 'Volver'
        back_button_icon = QIcon(dirImagenes+'/volver.png')
        back_button = QPushButton(self)
        back_button.setFixedSize(QSize(500, 200))
        
        back_button.setIcon(back_button_icon)
        # Establecer el tamaño del icono
        back_button.setIconSize(QSize(300, 200))
        back_button.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")

        back_button.clicked.connect(self.back_to_previous_screen)
        back_button.move(int(self.width / 3) - int(back_button.width()),1150)

        boton = QPushButton('Siguiente', self)
        boton.setStyleSheet("font-family: Century Gothic; font-size: 40px; border: none; border-radius: 50px; padding: 10px; background-color: #F0DE9A; color: #00416A; ")
        boton.setFixedSize(QSize(500, 200))
        boton.move(int(self.width / 2) + 400, 1150)

        self.show()

    def back_to_previous_screen(self):
        self.hide()
        self.previous_screen = ScreenModulos()
        self.previous_screen.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())