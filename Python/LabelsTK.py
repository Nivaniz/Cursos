from tkinter import *

# Para iniciar la carpeta raíz
root = Tk()

# Para imagenes
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack()

'''
# String bars dinámicas
texto = StringVar()
texto.set("ABOUT US")

# Configurar atributos
root.title("Labels")  # Título
root.iconbitmap("hola.ico")  # Icono

# Frame
frame = Frame(root, width=480, height=320)
frame.pack()

Label(frame, text="Vendemos muchas cosas").place(x=150, y=150)

Label(root, text="HOME").place(x=5, y=3) # Ponerlo en tal lugar
label1 = Label(root)
label1.place(x=80, y=3)
Label(root, text="CONTACT").place(x=155, y=3)

# Atributos
label1.config(bg="green", fg="blue", font=("Verdana", 10))
label1.config(textvariable=texto)
'''

# Finalizar
root.mainloop()