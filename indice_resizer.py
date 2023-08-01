# INDICE ALternativo
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Bienvenidos al Cactus World Tour')
#root.iconbitmap('/img/icono.ico')
root.geometry('1322x831')

#Definimos Image de fondo
bg = ImageTk.PhotoImage(file="img/back2.png")

#Creamos canvas
my_canvas = Canvas(root, width=1322, height=831)
my_canvas.pack(fill='both', expand=True)

#Poner imagenes en Canvas
my_canvas.create_image(0,0, image = bg, anchor="nw")

#Agregamos Label
my_canvas.create_text(700, 300, text= 'Cactus Tour Musical', font=("Bahamas",36), fill="white")
my_canvas.create_text(700, 350, text= 'En los proximos meses tendremos muchas novedades para ustedes', font=("Bahamas",27), fill="white")
my_canvas.create_text(700, 400, text= 'Vea nuestra cartelera', font=("Bahamas",27), fill="white")

#Agregando Botones
button1 = Button(root, text='Agosto', font=('bahamas',14))
button2 = Button(root, text='Septiembre', font=('bahamas',14))
button3 = Button(root, text='Octubre', font=('bahamas',14))
button4 = Button(root, text='Noviembre', font=('bahamas',14))
button5 = Button(root, text='Diciembre', font=('bahamas',14))

button1_windows = my_canvas.create_window(10, 500, anchor='nw', window= button1)
button2_windows = my_canvas.create_window(10, 550, anchor='nw', window= button2)
button3_windows = my_canvas.create_window(10, 600, anchor='nw', window= button3)
button4_windows = my_canvas.create_window(10, 650, anchor='nw', window= button4)
button5_windows = my_canvas.create_window(10, 700, anchor='nw', window= button5)

def resizer(e):
    global bg1, resized_bg, new_bg
    #Imegen
    bg1 = Image.open("img/back2.png")
    #Resize the image
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    #Definir 2da vez Imagen
    new_bg = ImageTk.PhotoImage(resized_bg)
    #Agregar de nuevo en canvas
    my_canvas.create_image(0,0, image = new_bg, anchor="nw")
    #Agregar texto Resize
    my_canvas.create_text(700, 300, text= 'Cactus Tour Musical', font=("Bahamas",36), fill="white")
    my_canvas.create_text(700, 350, text= 'En los proximos meses tendremos muchas novedades para ustedes', font=("Bahamas",27), fill="white")
    my_canvas.create_text(700, 400, text= 'Vea nuestra cartelera', font=("Bahamas",27), fill="white")


root.bind('<Configure>', resizer)
root.mainloop()