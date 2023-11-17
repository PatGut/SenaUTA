import csv
import copy
import argparse

import cv2 as cv
import mediapipe as mp
from collections import deque

from utils import cvfpscalc
from utils import draw
from utils import landmark
from model.HandClassifier.HandClassifier import handClassifier

import tkinter as tk
import imutils
from PIL import Image, ImageTk

import threading
import time

subtitle = ''
timesCaptured = 0
prevChar = ''
video = None
locker = threading.Event()

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
    args = parser.parse_args()
    return args

def createSpace():
    global subtitle
    subtitle += ' '
    return

def time_Captured(char, times):
    global timesCaptured
    global prevChar
    global subtitle
    if timesCaptured == 10:
        subtitle += char
    if char == prevChar:
        times += 1
        return times
    else:
        prevChar = char
        return 0
    
def erasesubtitle():
    global subtitle
    subtitle = ''
    return


def main():
    global locker
    def video_stream():
        global video
        global locker
        # Parsing de Argumentos #################################################################
        args = get_args()
        use_static_image_mode = args.use_static_image_mode
        min_detection_confidence = args.min_detection_confidence
        min_tracking_confidence = args.min_tracking_confidence    
        mp_hands = mp.solutions.hands
        
        hands = mp_hands.Hands(static_image_mode = use_static_image_mode,
            max_num_hands = 1,
            min_detection_confidence = min_detection_confidence,
            min_tracking_confidence = min_tracking_confidence
        )

        # Insertar modelo de clasificación
        
        hand_classifier = handClassifier()
        
        #Leer Labels
        with open('model/HandClassifier/hand_label.csv',
                encoding='utf-8-sig') as f:
            keypoint_classifier_labels = csv.reader(f)
            keypoint_classifier_labels = [
                row[0] for row in keypoint_classifier_labels
            ]
        # medir FPS
        cvFpsCalc = cvfpscalc.CvFpsCalc(buffer_len=10)    
        # Preparar la Camara
        while True:
            locker.wait()
            time.sleep(1)
            getVideo(hands,keypoint_classifier_labels, hand_classifier, cvFpsCalc, True)

        
    def getVideo(hands, keypoint_classifier_labels, hand_classifier, cvFpsCalc, use_brect):
        global timesCaptured
        global video
        
        #Capturar Camara #################################
        while True:
            fps = cvFpsCalc.get()   
            ret, image = video.read()
            if ret == True:
                image = cv.flip(image, 1) # Mostrar espejo de la camara
                debug_image = copy.deepcopy(image)
                #Funciona mejor con imagen a color
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                if results.multi_hand_landmarks is not None:
                    for hand_landmarks,handness in zip(results.multi_hand_landmarks,
                                                    results.multi_handedness):
                        # calcular bordes de las manos
                        brect = landmark.calc_bounding_rect(debug_image, hand_landmarks)
                        # Calcular Puntos de referencias
                        landmark_list = landmark.calc_landmark_list(debug_image, hand_landmarks)
                        #Convertir a cordenadas relativas / normalizada
                        pre_processed_landmark_list = landmark.pre_process_landmark(
                            landmark_list)
                        #Clasificación de la mano
                        mano_senial_id = hand_classifier(pre_processed_landmark_list)
                        #Dibujar
                        debug_image = draw.draw_bounding_rect(use_brect, debug_image, brect)
                        debug_image = draw.draw_landmarks(debug_image, landmark_list)
                        timesCaptured = time_Captured(str(keypoint_classifier_labels[mano_senial_id]),timesCaptured)
                        debug_image = draw.draw_info_text(
                            debug_image,
                            brect,
                            handness,
                            keypoint_classifier_labels[mano_senial_id]
                        )
                        
                        textsize = cv.getTextSize(subtitle, cv.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
                        textX = (debug_image.shape[1] - textsize[0]) / 2
                        debug_image = cv.putText(
                            debug_image,
                            subtitle,
                            (int(textX),450),
                            cv.FONT_HERSHEY_SIMPLEX,
                            1,
                            (255,255,0),
                            2,
                            cv.LINE_AA
                        )
                debug_image = draw.draw_info(debug_image, fps)
                debug_image = cv.resize(debug_image,(840,485))
                debug_image_tk = cv.cvtColor(debug_image, cv.COLOR_BGR2RGB)
                img = Image.fromarray(debug_image_tk)
                image = ImageTk.PhotoImage(image=img)
                etiq_de_video.configure(image=image)
                etiq_de_video.image = image
            else:
                print('img no capturada')
                break
    
    def quitar():
        global video
        etiq_de_video.place_forget()
        video.release()
        locker.clear()
        return
    
    def activateVideo():
        global video
        args = get_args()
        cap_device = args.device
        cap_width = args.width
        cap_height = args.height
        etiq_de_video.place(x=77,y=95)
        video = cv.VideoCapture(cap_device)
        video.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
        video.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)
        locker.set()
        return
    
    #Realizar un thread separado para el video
    thread_video = threading.Thread(target = video_stream)
    thread_video.daemon = True # Muere cuando el thread (la cual no pertenezca a los daemon) salga.
    locker.clear()
    thread_video.start()
    # Tkinter
    ventana = tk.Tk()
    ventana.geometry("1000x680+200+10")
    ventana.title("Reconocimiento del lenguaje de señas chileno")
    ventana.resizable(width=False, height=False)
    fondo = tk.PhotoImage(file ="./MainUI.png")
    fondo1 = tk.Label(ventana, image=fondo).place(x=0,y=0, relwidth=1, relheight=1)
    #Colores
    fondo_boton = '#f67e7d'
    #Botones
    boton = tk.Button(ventana, text="Reiniciar\n Subtítulos", bg=fondo_boton, relief="flat",
                    cursor="hand2", width=10, height=2, command=erasesubtitle,font=("Calisto MT",14,"bold"))
    boton.place(x=200,y=600)

    boton2 = tk.Button(ventana, text="Quitar\n Video", bg=fondo_boton, relief="flat",
                    cursor="hand2", width=10, height=2, command =quitar ,font=("Calisto MT",14,"bold"))
    boton2.place(x=350,y=600)

    boton3 = tk.Button(ventana, text="Iniciar\n Video", bg=fondo_boton, relief="flat",
                    cursor="hand2", width=10, height=2, command=activateVideo,font=("Calisto MT",14,"bold"))
    boton3.place(x=500,y=600)
    
    boton4 = tk.Button(ventana, text="Crear\n Espacio", bg=fondo_boton, relief="flat",
                    cursor="hand2", width=10, height=2, command=createSpace,font=("Calisto MT",14,"bold"))
    boton4.place(x=650,y=600)

    #Etiqueta de video
    etiq_de_video = tk.Label(ventana, bg="#5e17eb")
    
    
    
    ventana.mainloop()
    
    
if __name__ == '__main__':
    main_thread = threading.Thread(target = main)
    main_thread.daemon = False
    main_thread.start()


