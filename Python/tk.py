from tkinter import *

''' INICIALIZACIÓN '''
# Para iniciar la carpeta raíz
root = Tk()
# Configurar atributos
root.title("Cafetería")  # Título
root.iconbitmap("hola.ico")  # Icono
# root.resizable(False, False)  # Sí se puede redimensionar alto y ancho
root.resizable(True, True)

''' FRAME '''
frame = Frame(root)  # Tener dentro de la raíz
# Lo empaqueté y lo distribuya
# frame.pack(side="bottom", anchor="e")  # Los alinea arriba y en medio automaticamete

frame.pack(fill='both', expand=1)  # Ancho del padre y que utilicé lo mismo

# Otorgamos tamaño
frame.config(width=480, height=320)
frame.config(cursor="pirate")  # cambia el cursor encima de la ventana como calavera
frame.config(bg="lightblue")  # Cambiar el fondo de color
frame.config(bd=25)  # Tamaño de borde
frame.config(relief="sunken")  # Agrega borde personalizado


''' ROOT '''
root.config(width=480, height=320)
root.config(cursor="arrow")  # cambia el cursor encima de la ventana como calavera
root.config(bg="blue")  # Cambiar el fondo de color
root.config(bd=15)  # Tamaño de borde
root.config(relief="sunken")

root.mainloop()  # Final
