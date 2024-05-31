import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'actividad 1.png'
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(binary, kernel, iterations = 1)

dilation = cv2.dilate(erosion, kernel, iterations = 1)

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title("Imagen Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Imagen en Escala de Grises")
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Umbralización")
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Resultado de Morfología (Erosión + Dilatación)")
plt.imshow(dilation, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

