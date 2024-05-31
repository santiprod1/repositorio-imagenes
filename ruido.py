import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("ruido.jpg", cv2.IMREAD_GRAYSCALE)

plt.imshow(img,cmap="gray")
plt.show()
ret1,th1 = cv2.thresold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(th1,cmap="gray")
plt.show()

plt.hist(img.flatten(),256)
plt.show()

ret2,th2 = cv2.thresold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(th2,cmap="gray")
plt.show()

blur = cv2.GaussianBlur(img,(7,7),0)
plt.imshow(blur,cmap="gray")
plt.show()
plt.hist(blur.flatten(),256)
plt.show()
ret2,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(th3,cmap="gray")
plt.show()