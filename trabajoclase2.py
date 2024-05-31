import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-500, 501, 1)
longitudes_onda = [100, 150, 200, 250, 300, 350]
angulos = [np.pi/6, np.pi/4, np.pi/3, np.pi/2, 3*np.pi/4, np.pi]

X, Y = np.meshgrid(x, x)
gradientef = np.zeros_like(X, dtype=float)

for longitudOnda, angulo in zip(longitudes_onda, angulos):
    gradiente = np.sin(2 * np.pi * (X * np.cos(angulo) + Y * np.sin(angulo)) / longitudOnda)
    gradientef += gradiente

plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.imshow(gradientef, cmap="gray")
plt.title("Imagen de la suma de sinusoidales")

fourier = np.fft.fft2(gradientef)
fourier = np.fft.fftshift(fourier)
plt.subplot(122)
plt.imshow(np.abs(fourier), cmap="gray")
plt.title("Transformada de Fourier")

plt.xlim([480, 520])
plt.ylim([520, 480])

plt.savefig('/mnt/data/suma_sinusoidales_fourier.png')
plt.show()
