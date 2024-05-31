import numpy as np
import cv2
 
camara = cv2.VideoCapture(0)
fondo = None
 
while True:
    ret, cuadro = camara.read()
    gris = cv2.cvtColor(cuadro, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (15, 15), 0)
   
    if fondo is None:
        fondo = gris
        continue
    resta = cv2.absdiff(fondo, gris)
    cv2.imshow('resta', resta)
    umbral = cv2.threshold(resta, 30, 255, cv2.THRESH_BINARY)[1]
    umbral = cv2.dilate(umbral, None, iterations=2)
    contornos, hierarchy = cv2.findContours(umbral, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
 
    for c in (contornos):
        if cv2.contourArea(c) < 500:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(cuadro, (x, y), (x+w, y+h), (0, 255, 0), 2)
       
    cv2.imshow('umbral', umbral)
    cv2.imshow('Final', cuadro)
   
    if cv2.waitKey(1) == ord('q'):
        print('Salida')
        break
 
camara.release()
 
cv2.waitKey()
cv2.destroyAllWindows()