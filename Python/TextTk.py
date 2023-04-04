from tkinter import *

root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Consolas", 12), padx=45, pady=15, selectbackground="red")  # Lee numeros de
# caracteres y no de tamaño
root.mainloop()