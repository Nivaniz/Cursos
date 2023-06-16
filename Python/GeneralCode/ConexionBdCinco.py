import tkinter as tk
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("usuariosai.db")
cursor = conexion.cursor()

class AgregarRegistro:
    def __init__(self, parent):
        self.parent = parent
        self.top = tk.Toplevel(parent)

        # Crear los campos de entrada para cada columna de la base de datos
        self.dni_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.edad_var = tk.StringVar()
        self.gmail_var = tk.StringVar()

        dni_label = tk.Label(self.top, text="DNI:")
        dni_label.pack()
        dni_entry = tk.Entry(self.top, textvariable=self.dni_var)
        dni_entry.pack()

        nombre_label = tk.Label(self.top, text="Nombre:")
        nombre_label.pack()
        nombre_entry = tk.Entry(self.top, textvariable=self.nombre_var)
        nombre_entry.pack()

        edad_label = tk.Label(self.top, text="Edad:")
        edad_label.pack()
        edad_entry = tk.Entry(self.top, textvariable=self.edad_var)
        edad_entry.pack()

        gmail_label = tk.Label(self.top, text="Gmail:")
        gmail_label.pack()
        gmail_entry = tk.Entry(self.top, textvariable=self.gmail_var)
        gmail_entry.pack()

        # Botón para agregar el registro a la base de datos
        agregar_button = tk.Button(self.top, text="Agregar registro", command=self.agregar_registro)
        agregar_button.pack()

    def agregar_registro(self):
        # Obtener los valores de los campos de entrada
        dni = self.dni_var.get()
        nombre = self.nombre_var.get()
        edad = self.edad_var.get()
        email = self.gmail_var.get()

        # Insertar el nuevo registro en la base de datos
        cursor.execute("INSERT INTO usuariosai (dni, nombre, edad, email) VALUES (?, ?, ?, ?)", (dni, nombre, edad, email))
        conexion.commit()

        # Cerrar la ventana de agregar registro
        self.top.destroy()

class BorrarRegistro:
    def __init__(self, parent):
        self.parent = parent
        self.top = tk.Toplevel(parent)

        # Crear un campo de entrada para el ID del registro a borrar
        self.id_var = tk.StringVar()

        id_label = tk.Label(self.top, text="ID del registro:")
        id_label.pack()
        id_entry = tk.Entry(self.top, textvariable=self.id_var)
        id_entry.pack()

        # Botón para borrar el registro de la base de datos
        borrar_button = tk.Button(self.top, text="Borrar registro", command=self.borrar_registro)
        borrar_button.pack()

    def borrar_registro(self):
        # Obtener el valor del campo de entrada del ID del registro a borrar
        id = self.id_var.get()

        # Borrar el registro correspondiente de la la base de datos
        cursor.execute("DELETE FROM usuariosai WHERE id=?", (id,))
        conexion.commit()

        # Cerrar la ventana de borrar registro
        self.top.destroy()


class VentanaPrincipal:
    def __init__(self, parent):
        self.parent = parent

        # Botón para agregar un nuevo registro
        agregar_button = tk.Button(parent, text="Agregar registro", command=self.abrir_agregar_registro)
        agregar_button.pack()

        # Botón para borrar un registro existente
        borrar_button = tk.Button(parent, text="Borrar registro", command=self.abrir_borrar_registro)
        borrar_button.pack()

    def abrir_agregar_registro(self):
        # Crear la ventana de agregar registro
        AgregarRegistro(self.parent)

    def abrir_borrar_registro(self):
        # Crear la ventana de borrar registro
        BorrarRegistro(self.parent)

# Crear ventana principal
root = tk.Tk()
root.title("Usuarios AI")
VentanaPrincipal(root)
root.mainloop()
conexion.close()
