from tkinter import *

# Raíz creada
root = Tk()

# Manejo de información
# Campos Alineados a la izquierda
label = Label(root, text="Nombre(s)")
label.grid(row=0, column=0, sticky="e", padx=5, pady=5 )

entrada = Entry(root)
entrada.grid(row=0, column=1)

label2 = Label(root, text="Apellido Paterno")
label2.grid(row=1, column=0,  sticky="e", padx=5, pady=5)

entrada2 = Entry(root)
entrada2.grid(row=1, column=1)

label3 = Label(root, text="Contraseña")
label3.grid(row=2, column=0,  sticky="e", padx=5, pady=5)

entrada3 = Entry(root)
entrada3.grid(row=2, column=1)
entrada3.config(justify="center", show="*")

# Finalmente bucle de la aplicación
root.mainloop()
