from tkinter import *


def hola():
    print("Hola!")


def crear_label():
    Label(root, text="Label creada").pack()


root = Tk()
Button(root, text="Accede", command=hola).pack()
Button(root, text="Salir", command=crear_label).pack()

root.mainloop()