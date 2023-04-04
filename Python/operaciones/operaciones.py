def sumar(a, b):
    try:
        resultado = a + b
        print(f"La suma de {a} y {b} es igual a {resultado}")
    except TypeError:
        print("Error: Debes ingresar dos números para realizar la suma.")

def restar(a, b):
    try:
        resultado = a - b
        print(f"La resta de {a} y {b} es igual a {resultado}")
    except TypeError:
        print("Error: Debes ingresar dos números para realizar la resta.")

def multiplicar(a, b):
    try:
        resultado = a * b
        print(f"La multiplicación de {a} y {b} es igual a {resultado}")
    except TypeError:
        print("Error: Debes ingresar dos números para realizar la multiplicación.")

def dividir(a, b):
    try:
        resultado = a / b
        print(f"La división de {a} y {b} es igual a {resultado}")
    except ZeroDivisionError:
        print("Error: No puedes dividir entre cero.")
    except TypeError:
        print("Error: Debes ingresar dos números para realizar la división.")
