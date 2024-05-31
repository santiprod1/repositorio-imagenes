import tkinter as tk
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt

win = tk.Tk()
win.geometry("750x550")
win.title("Visor de Imágenes")

def load_image():
    global foto  
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if filepath:
        foto = cv2.imread(filepath)
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

def show_image(mode):
    if not 'foto' in globals():
        print("Carga una imagen primero.")
        return

    if mode == "original":
        plt.imshow(cv2.cvtColor(foto, cv2.COLOR_BGR2RGB))
    elif mode == "rojo":
        plt.imshow(foto[:,:,2], cmap='Reds')
    elif mode == "verde":
        plt.imshow(foto[:,:,1], cmap='Greens')
    elif mode == "azul":
        plt.imshow(foto[:,:,0], cmap='Blues')
    elif mode == "blanco_y_negro":
        gray_image = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
        plt.imshow(gray_image, cmap='gray')
    plt.title(mode)
    plt.show()

entry = tk.Entry(win, width=50)
entry.pack(pady=10)

btn_load = tk.Button(win, text="Cargar Imagen", command=load_image)
btn_load.pack(pady=10)

btn_original = tk.Button(win, text="Imagen Original", command=lambda: show_image("original"))
btn_original.pack(pady=10)

btn_rojo = tk.Button(win, text="Canal Rojo", command=lambda: show_image("rojo"))
btn_rojo.pack(pady=10)

btn_verde = tk.Button(win, text="Canal Verde", command=lambda: show_image("verde"))
btn_verde.pack(pady=10)

btn_azul = tk.Button(win, text="Canal Azul", command=lambda: show_image("azul"))
btn_azul.pack(pady=10)

btn_bn = tk.Button(win, text="Blanco y Negro", command=lambda: show_image("blanco_y_negro"))
btn_bn.pack(pady=10)

win.mainloop()

