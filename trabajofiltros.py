import tkinter as tk
import cv2
import numpy as np
import matplotlib.pyplot as plt

win = tk.Tk()
win.geometry("750x550")
win.title("Visor de Imágenes")

image_paths = {
    "image1": "image1.jpg",
    "image2": "image2.jpg",
    "image3": "image3.jpg"
}

def apply_sepia(image):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia = cv2.transform(image, kernel)
    return sepia

def apply_sharpen(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

def apply_edge(image):
    edges = cv2.Canny(image, 100, 200)
    return edges

def apply_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def apply_invert(image):
    inverted = cv2.bitwise_not(image)
    return inverted

def apply_brightness(image, delta=30):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, delta)
    final_hsv = cv2.merge((h, s, v))
    img_bright = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img_bright

def show_image(mode, image_key):
    foto = cv2.imread(image_paths[image_key])
    
    filter_map = {
        "original": lambda x: cv2.cvtColor(x, cv2.COLOR_BGR2RGB),
        "sepia": apply_sepia,
        "sharpen": apply_sharpen,
        "edge": apply_edge,
        "grayscale": apply_grayscale,
        "invert": apply_invert,
        "brightness": apply_brightness
    }
    
    result = filter_map[mode](foto)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title(mode)
    plt.show()

btn_sepia1 = tk.Button(win, text="Sepia Imagen 1", command=lambda: show_image("sepia", "image1"))
btn_sepia1.pack(pady=10)
btn_brightness1 = tk.Button(win, text="Aclarar Imagen 1", command=lambda: show_image("brightness", "image1"))
btn_brightness1.pack(pady=10)

btn_sharpen2 = tk.Button(win, text="Nitidez Imagen 2", command=lambda: show_image("sharpen", "image2"))
btn_sharpen2.pack(pady=10)
btn_edge2 = tk.Button(win, text="Bordes Imagen 2", command=lambda: show_image("edge", "image2"))
btn_edge2.pack(pady=10)

btn_gray3 = tk.Button(win, text="Gris Imagen 3", command=lambda: show_image("grayscale", "image3"))
btn_gray3.pack(pady=10)
btn_invert3 = tk.Button(win, text="Invertir Imagen 3", command=lambda: show_image("invert", "image3"))
btn_invert3.pack(pady=10)

win.mainloop()
