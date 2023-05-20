# Excepciones
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Enter a number")
except ZeroDivisionError:
    print("Age can´t be 0")

# TypeErrror

# Para manejar errores

while (True):
    try:
        n = float(input("Introduce un num: "))
        m = 5
        print("{}/{}={}".format(n, m, n / m))
    except:  # Codigo excepcional
        print("Mete el numero bien")
    else:  # Código que se ejecutara si no existe un error
        print("Todo ha funcionado correctamente")
        break
    finally:  # Ocurra o no una iteración
        print("Fin de la iteración")


# Multiples excepciones
try:
    n = input("Introduce un número: ")
    5/n
except Exception as e:
    print(type(e).__name__)  # Mostrar el error sin que se deje de ejecutar el código

# Invocacion de excepciones
def fun(algo=None):
    try:
        if algo is None:
            raise ValueError("No se permiten valor nulo")
    except ValueError:
        print("No se permiten valor nulo (desde la excepcion)")

fun("algo")  # all good
fun()  # No se permiten valor nulo desde consola