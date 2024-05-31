import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('estacion.png', cv2.IMREAD_GRAYSCALE)
 
gaus = cv2.GaussianBlur(img, (19,19), 0)
 
Z = np.concatenate((img, gaus), axis=1)
 
Id = img.astype(float)
 
Ld = gaus.astype(float)
 
Hd = Id - Ld
 
H = np.abs(Hd)
H = H - np.min(H)
H = H / np.max(H) * 255
plt.imshow(H,cmap="gray")
plt.show()

Z = np.concatenate((img,H),axis=1)
plt.imshow(Z,cmap="gray")
plt.show()
 
E = (H>60)*255
plt.imshow(Z,cmap="gray")
plt.show()
 
plt.imshow(Z, cmap='gray')
plt.show()