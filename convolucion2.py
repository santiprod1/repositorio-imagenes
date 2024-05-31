
import numpy as np 
import cv2  as cv
import matplotlib.pyplot as plt

n = 1000
i = np.array(range(n,))
t = i*np.pi/n*8

x1 = np.sin(t)
x2 = 0.3*np.sin(20*t)
x = x1+x2
r = 0.2*(np.random.random_sample(size=n) - 0.5)
z = x + r

r = 0.2*(np.random.random_sample(size = n)-0.5)
plt.figure(figsize=(20,9))
plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,x)
plt.plot(t,z)
plt.legend(["x1","x2","ruido"])
plt.show()
m = 25
h1 = cv.getGaussianKernel(m,7)
h2 = cv.getGaussianKernel(m,1)
plt.plot(h1)
plt.plot(h2)
plt.legend(["h1","h2"])
plt.show()

y1 = np.convolve(z,h1[:,0],"same")
y2 = np.convolve(z,h2[:,0],"same")
plt.figure(figsize=(20,9))
plt.plot(t,y1)
plt.plot(t,y2)
plt.legend(["y1","y2"])
plt.show()
plt.figure(figsize=(20,9))
plt.plot(x1)
plt.plot(y1)
plt.plot(x1-y1)
plt.legend(["x1","y1","error"])
plt.show()

plt.figure(figsize=(20,9))
plt.plot(x2)
plt.plot(y2-y1)
plt.plot(x2-(y2-y1))
plt.legend(["x2","salida","error"])
plt.show()