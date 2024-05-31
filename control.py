import cv2
import numpy as np
import matplotlib.pyplot as plt

original_image = cv2.imread('casa.jpeg')

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

_, threshold_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

colored_image = original_image.copy()

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 128, 255), (255, 128, 128)]

for i, contour in enumerate(contours):
    if cv2.contourArea(contour) > 100: 
        cv2.drawContours(colored_image, [contour], -1, colors[i % len(colors)], -1)

cv2.imshow('Original Image', original_image)
cv2.imshow('Threshold Image', threshold_image)
cv2.imshow('Colored Image', colored_image)

cv2.imwrite('casa1.jpeg', original_image)
cv2.imwrite('casa2.jpeg', threshold_image)
cv2.imwrite('casa3.jpeg', colored_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
