# Buscar un número común en la expresión y readaptarla

num = 101
if 0 <= num <= 100:
    print("El número {} se encuentra entre 0 y 100".format(num))
else:
    print("El número {} no se encuentra entre 0 y 100".format(num))

# Comprensión de listas

'''
Método tradicional
lista = []
for letra in 'casa':
    lista.append(letra)
    
print(lista)
'''

lista = [letra for letra in 'casa']
print(lista)  # ['c', 'a', 's', 'a']

list = [numero ** 2 for numero in range(0, 11)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(list)

lis = [numero for numero in range(0, 11) if numero % 2 == 0]  # [0, 2, 4, 6, 8, 10]
print(lis)

li = [numero for numero in [numero ** 2 for numero in range(0, 11)] if numero % 2 == 0]  # [0, 4, 16, 36, 64, 100]
print(li)

''''
La primera da [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100] y la segunda if [0, 4, 16, 36 ...]
'''


# Funciones decoradoras


def hola():  # Función Global

    def bienvenido():  # Función Local
        return "Hola!"

    # print(locals())
    return bienvenido


hola()  # {'bienvenido': <function hola.<locals>.bienvenido at 0x0000028BA24D9260>}
print(hola()())  # Ya ejecuta el bienvenido
print("----------------------")
bienvenido = hola()
print(bienvenido())  # Hola!


def adios():
    return "Adios!"


def test(funcion):
    print(funcion())


test(adios)
print("__________________")


def monitorizar(funcion):
    def decorar(*args, **kwargs):
        print("Se esta apunto de ejecutar la funcion: ", funcion.__name__)
        funcion(*args, **kwargs)
        print("Se ha finalizado la ejecucion la funcion: ", funcion.__name__)

    return decorar


@monitorizar
def pepe(nombre):
    print("Soy Pepe, mucho gusto {}!".format(nombre))


@monitorizar
def saul(nombre):
    print("Soy Saul, mucho gusto {}!".format(nombre))


'''
monitorizar(pepe)()  # Llamada correcta, sin paréntesis adicionales
Se esta apunto de ejecutar la funcion:  decorar
Se esta apunto de ejecutar la funcion:  pepe
Pepe, hola!
Se ha finalizado la ejecucion la funcion:  pepe
Se ha finalizado la ejecucion la funcion:  decorar
'''

print("______________-")
pepe("Samantha")

'''
Se esta apunto de ejecutar la funcion:  pepe
Soy Pepe, mucho gusto Samantha!
Se ha finalizado la ejecucion la funcion:  pepe'''

# Funciones generadoras e iteradoras
print("______________-")


def pares(n):
    for numero in range(n+1):
        if numero%2 == 0:
            yield numero


'''yield se utiliza para crear un generador que produce 
una secuencia de valores y pausa la ejecución de la función en cada yield.'''

print(pares(10))  # Se obtiene un objeto generador <generator object pares at 0x000001E6C8B4DB60>
for numero in pares(20):
    print(numero, end=' ')  # 0 2 4 6 8 10 12 14 16 18 20


print("______________-")
# DE UNA MEJOR MANERA
print([numero for numero in pares(10)])  # [0, 2, 4, 6, 8, 10]

pares = pares(3)
print(next(pares))  # Nos da el primer elemento 0 solo funciona con elementos iteradores
print(next(pares))  # Nos da el primer elemento 2

# Colecciones a iteradores
listam = [1, 2, 3, 4, 5]
lista_iterable = iter(listam)  # Funciona con strings

print(next(lista_iterable))  # 1... 2... 3
