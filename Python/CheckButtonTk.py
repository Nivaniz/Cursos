from tkinter import *


def pedir_orden():
    global orden_window  # Declarar la variable como global
    orden = ""
    if leche.get():
        orden += "Con leche"
    else:
        orden += "Sin leche"

    if azucar.get():
        orden += ", con azúcar"
    else:
        orden += ", sin azúcar"

    root.withdraw()  # Ocultar la ventana raíz
    orden_window = Toplevel(root)
    orden_window.title("Su orden")
    orden_window.geometry("300x400")
    Label(orden_window, text="Su orden es: " + orden).pack(pady=20)
    orden_window.protocol("WM_DELETE_WINDOW", volver_a_raiz)  # Acción al cerrar la ventana


def volver_a_raiz():
    root.deiconify()  # Mostrar la ventana raíz
    orden_window.destroy()  # Cerrar la ventana actual


root = Tk()
root.title("Cafetería")
root.config(bd=15)
root.option_add("*Font", "Arial 12")

leche = IntVar()  # 1 si, 0 no
azucar = IntVar()  # 1 si, 0 no

imagen = PhotoImage(file="imagen.gif")
label_imagen = Label(root, image=imagen)
label_imagen.pack(side="left")

frame = Frame(root)
frame.pack(side="right")

Label(root, text="¿Cómo quieres el cafe?").pack(anchor="w")
Checkbutton(root, text="Con leche", variable=leche, onvalue=1, offvalue=0).pack(anchor="w")
Checkbutton(root, text="Con azúcar", variable=azucar, onvalue=1, offvalue=0).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

pedir_orden_button = Button(root, text="Pedir orden", command=pedir_orden)
pedir_orden_button.pack(side="bottom")

root.mainloop()

