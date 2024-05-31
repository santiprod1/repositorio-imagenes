import numpy as np 
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cebra.jpg")

plt.imshow(img,cmap="gray")

m= 25
h1 = cv2.getGaussianKernel(m,7)
g= np.ones((m,))/m
N,M = img.shape
Y = np.zeros((N,M))
Y2 = np.zeros((N,M))


for i in range (N):
    Y[i,:] = np.convolve(img[i,:],g,"same")
    plt.imshow(Y,cmap="gray")
    plt.show()
    
for i in range (N):
    Y2[i,:] = np.convolve(img[i,:],h1[:,0],"same")
    
plt.imshow(Y2,cmap="gray")
plt.show()  