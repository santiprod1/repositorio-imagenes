import numpy as np
import cv2
import matplotlib.pyplot as plt
 
img = cv2.imread("river.png")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
 
img_blur = cv2.GaussianBlur(rgb, (3,3), 0)
plt.imshow(img_blur)
plt.show()
laplace = cv2.Laplacian(img_blur, cv2.CV_64F)
plt.imshow(laplace)
plt.show()
sobel_x = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, ksize=15)
plt.imshow(sobel_x)
plt.show()
sobel_y = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, ksize=15)
plt.imshow(sobel_y)
plt.show()
 
suma = sobel_x + sobel_y
plt.imshow(suma)
plt.show()
 
sharpened_img = rgb - 0.7 * laplace
sharpened_img = np.clip(sharpened_img, 0, 255)  
plt.imshow(sharpened_img.astype(np.uint8))
plt.show()