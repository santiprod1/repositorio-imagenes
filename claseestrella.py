import cv2
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread("engranaje.webp")
img2 = cv2.imread("engranaje.webp",cv2.IMREAD_GRAYSCALE)
 
ret, thresh = cv2.threshold(img2, 240, 255, cv2.THRESH_BINARY_INV)
contours,hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
plt.imshow(thresh)
plt.show()
cnt = contours[2]
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.0018*perimeter
approx = cv2.approxPolyDP(cnt,epsilon,True)
hull = cv2.convexHull(approx,True)
cv2.drawContours(img,[hull],-1,255,3)
plt.imshow(img)
plt.show()