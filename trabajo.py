import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('figuras.png')
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
ret,thresh = cv2.threshold(gris, 225, 255, cv2.THRESH_BINARY)
countours2, hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, countours2, -1, (50,150,0), 4)
figura = 0
 
for c in countours2:
    x,y,w,h = cv2.boundingRect(c)
    area = cv2.contourArea(c)
    if (area>1000):
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,0), 2)
        cv2.putText(img, f"figura {figura}", (x,y),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        figura += 1
 
cv2.imshow('figuras', img)
cv2.imshow('gris', thresh)
cv2.waitKey()
cv2.destroyAllWindows()