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
import threading

subtitle = ''
timesCaptured = 0
prevChar = ''
video = None

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
    


def main():
    def video_stream():
        global timesCaptured
        args = get_args()  # Asegúrate de que get_args() está definida y devuelve los argumentos correctos
        video = cv.VideoCapture(args.device)
        video.set(cv.CAP_PROP_FRAME_WIDTH, args.width)
        video.set(cv.CAP_PROP_FRAME_HEIGHT, args.height)
        use_static_image_mode = args.use_static_image_mode
        min_detection_confidence = args.min_detection_confidence
        min_tracking_confidence = args.min_tracking_confidence    
        mp_hands = mp.solutions.hands
        
        hands = mp_hands.Hands(static_image_mode = use_static_image_mode,
            max_num_hands = 2,
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

        while True:
            fps = cvFpsCalc.get()  
            ret, image = video.read()
            if not ret:
                print("No se pudo capturar el frame de la cámara")
                break
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
                    debug_image = draw.draw_bounding_rect(True, debug_image, brect)
                    debug_image = draw.draw_landmarks(debug_image, landmark_list)
                    timesCaptured = time_Captured(str(keypoint_classifier_labels[mano_senial_id]),timesCaptured)
                    '''debug_image = draw.draw_info_text(
                        debug_image,
                        brect,
                        handness,
                        keypoint_classifier_labels[mano_senial_id]
                    )'''
                    
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
            debug_image = cv.resize(debug_image,(800,600))
            # Mostrar el frame
            cv.imshow("Video", debug_image)

            # Verificar si se presiona 'q' para salir
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        video.release()
        cv.destroyAllWindows()


    
    
    
    #Realizar un thread separado para el video
    thread_video = threading.Thread(target = video_stream)
    thread_video.start()
    thread_video.join() 
    
    
    
if __name__ == '__main__':
    main()


