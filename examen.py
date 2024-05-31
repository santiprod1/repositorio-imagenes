import numpy as np
import cv2
import matplotlib.pyplot as plt
 
image1 = cv2.imread('amarilla.png')
image2 = cv2.imread('cielo.jpg')
 
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))
 
lower_blue = np.array([100, 0, 0])
upper_blue = np.array([255, 100, 100])
mask = cv2.inRange(image1, lower_blue, upper_blue)
 
img3 = cv2.addWeighted(image2, 0.3, image1, 2, 0)
 
cv2.equalizeHist(img3[:,:,2])
B, G, R = cv2.split(img3)
 
B = cv2.equalizeHist(B)
G = cv2.equalizeHist(G)
R = cv2.equalizeHist(R)
 
kernel = np.ones((2,2), np.uint8)
 
img3 = cv2.merge((B, G, R))
 
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50,50)
fontScale = 1
color = (150,0,0)
grosor = 1
texto = 'Andres Santiago Rojas Coria'
img3 = cv2.putText(img3, texto, org, font, fontScale, color, grosor, cv2.LINE_AA)
 
cv2.imshow('Imagen', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()