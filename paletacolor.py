import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: No se pudo leer el frame.")
        break
    
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    green_lower = np.array([35, 50, 50], np.uint8)
    green_upper = np.array([85, 255, 255], np.uint8)
    
    green_mask = cv.inRange(frame_hsv, green_lower, green_upper)
    
    solid_color = np.zeros_like(frame)
    solid_color[:] = [0, 255, 0]
    
    result_with_green = cv.bitwise_and(solid_color, solid_color, mask=green_mask)
    
    cv.imshow('Original', frame)
    cv.imshow('Solo Verde', result_with_green)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
