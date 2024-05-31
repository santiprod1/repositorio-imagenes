import tkinter as tk
import numpy as np 
import cv2 
import matplotlib.pyplot as plt

n = 1000
i = np.array(range(n,))
t = i*np.pi/n*8

x = np.sin(t)
y = np.sin(2*t)
x1 = x+y

r = np.random.random_sample(size = n)-0.5
plt.figure(figsize=(20,9))
plt.plot(t,x)
plt.plot(t,y)
plt.plot(t,x1)
plt.legend(["x","y","x1","r"])
plt.show()
xr = r + x1 
plt.figure(figsize=(20,9))
plt.plot(t,xr)
plt.show()

m = 15 
g = np.ones((m,))/m

y1 = np.convolve(xr,g, "same")
plt.figure(figsize=(20,9))
plt.plot(t,x1)
plt.plot(t,y1)
#plt.plot(t,xr)
plt.legend(["norm","conv"])
plt.show()