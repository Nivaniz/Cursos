import tkinter as tk


# Funciones de suma, resta, multiplicación y división
def sumar():
    resultado.set(round(float(numero1.get()) + float(numero2.get()), 2))


def restar():
    resultado.set(round(float(numero1.get()) - float(numero2.get()), 2))


def multiplicar():
    resultado.set(round(float(numero1.get()) * float(numero2.get()), 2))


def dividir():
    try:
        resultado.set(round(float(numero1.get()) / float(numero2.get()), 2))
    except ZeroDivisionError:
        resultado.set("Error: no se puede dividir entre cero")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variables de entrada y salida
numero1 = tk.StringVar()
numero2 = tk.StringVar()
resultado = tk.StringVar()

# Diseño de la calculadora
ventana.geometry("400x250")
ventana.configure(bg="#F5F5F5")
ventana.resizable(False, False)
ventana.iconbitmap("hola.ico")

# Estilos de fuente y color
fuente_calculo = ("Arial", 14, "bold")
fuente_resultado = ("Arial", 16)
color_boton = "#D9D9D9"
color_boton_hover = "#BFBFBF"
color_boton_presionado = "#A6A6A6"
color_fondo_boton = "#F5F5F5"
color_texto = "#333333"

# Widgets de entrada
tk.Label(ventana, text="Primer número: ", bg="#F5F5F5", fg=color_texto, font=fuente_calculo).grid(row=0, column=0,
                                                                                                  padx=5, pady=5)
tk.Entry(ventana, textvariable=numero1, font=fuente_calculo).grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Segundo número: ", bg="#F5F5F5", fg=color_texto, font=fuente_calculo).grid(row=1, column=0,
                                                                                                   padx=5, pady=5)
tk.Entry(ventana, textvariable=numero2, font=fuente_calculo).grid(row=1, column=1, padx=5, pady=5)

# Botones de operaciones
tk.Button(ventana, text="Sumar", command=sumar, bg=color_boton, activebackground=color_boton_presionado,
          fg=color_texto, activeforeground=color_texto, font=fuente_calculo, padx=10, pady=5,
          bd=0, highlightthickness=0, cursor="hand2").grid(row=2, column=0, padx=5, pady=5)

tk.Button(ventana, text="Restar", command=restar, bg=color_boton, activebackground=color_boton_presionado,
          fg=color_texto, activeforeground=color_texto, font=fuente_calculo, padx=10, pady=5,
          bd=0, highlightthickness=0, cursor="hand2").grid(row=2, column=1, padx=5, pady=5)

tk.Button(ventana, text="Multiplicar", command=multiplicar, bg=color_boton, activebackground=color_boton_presionado,
          fg=color_texto, activeforeground=color_texto, font=fuente_calculo, padx=10, pady=5, bd=0, highlightthickness=0,
          cursor="hand2").grid(row=3, column=0, padx=5, pady=5)

tk.Button(ventana, text="Dividir", command=dividir, bg=color_boton, activebackground=color_boton_presionado,
          fg=color_texto, activeforeground=color_texto, font=fuente_calculo, padx=10, pady=5,bd=0, highlightthickness=0,
          cursor="hand2").grid(row=3, column=1, padx=5, pady=5)

# Widgets de resultado
tk.Label(ventana, text="Resultado: ", bg="#F5F5F5", fg=color_texto, font=fuente_calculo).grid(row=4, column=0, padx=5, pady=5)
tk.Entry(ventana, textvariable=resultado, font=fuente_resultado, state="disable", readonlybackground="#FFFFFF").grid(row=4, column=1, padx=5, pady=5)

ventana.mainloop()