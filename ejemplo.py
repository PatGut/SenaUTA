import cv2 as cv

cap = cv.VideoCapture(1)  # Cambia el índice si es necesario
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar el frame de la cámara")
        break
    cv.imshow("Test Camera", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
