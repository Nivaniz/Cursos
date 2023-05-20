from tkinter import *
from tkinter import messagebox as MessagesBox
from tkinter import  colorchooser as Color
from tkinter import  filedialog as FileD

root = Tk()
root.title("Alerta")


def test():
    MessagesBox.showinfo("Alerta Emergente", "No se pudo continuar el proceso")


def test2():
    MessagesBox.showwarning("WARNING", "No se pudo continuar el proceso")


def test3():
    MessagesBox.showerror("Error", "No se pudo continuar el proceso")


def test4():
    resultado = MessagesBox.askquestion("Salir", "¿Estas seguro que quieres salir sin guardar?")
    if resultado == "yes":
        root.destroy()
    else:
        pass


def test5():
    resultado = MessagesBox.askokcancel("Salir", "¿Estas seguro que quieres salir?")
    if resultado:
        root.destroy()
    else:
        pass


def test6():
    Color.askcolor(title="Elige un color")  # Regresa una tupla RGB y el HEX


def test7():
    FileD.askopenfilename(title="Abrir un fichero", initialdir="D:", filetypes=(("Ficheros de texto", "*.txt"),
                                                                                ("Ficheros de texto avanzado", "*.txt2"),
                                                                                ("Todos los ficheros", "*.*")))  #
    # Abrir una ruta, la devuelve


def test8():
    ruta = FileD.asksaveasfilename(title="Guardar un fichero", defaultextension=".txt")  # Equivale a open('ruta, 'w')


Button(root, text="Alerta Emergente", command=test).pack()
Button(root, text="Warning", command=test2).pack()
Button(root, text="Error", command=test3).pack()
Button(root, text="Pregunta s/n", command=test4).pack()
Button(root, text="Pregunta aceptar/cancelar", command=test5).pack()
Button(root, text="Seleccionar color", command=test6).pack()
Button(root, text="Seleccionar fichero", command=test7).pack()
Button(root, text="Manejar una ruta", command=test8).pack()

root.mainloop()
