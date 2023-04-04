# Pilas / stacks
# Permiten añadir un elemento a la fila o sacarlo
# Ultimo en entrar, primero en salir

pila = [3, 4, 5]
pila.append(6)
pila.append(7)  # [3, 4, 5, 6, 7]

pila.pop()  # Para eliminarlo el ultimo de la fila
# [3, 4, 5, 6]

# Pero si quisieramos guardarlo este ultimo valor sería
n = pila.pop()  # n = 6

# Cola
# El primero en entrar es el primero en salir
from collections import deque

cola = deque()
cola = deque(['Hector', 'Juan', 'Miguel'])

cola.append('Maria')
cola.append('Armaldo')  # ['Hector', 'Juan', 'Miguel', 'Maria', 'Armaldo']

cola.popleft()  # Héctor

# Entradas de texto
v = "bonito"
n = 20
texto = "Un texto {} y un numero {}".format(v, n)
print(texto)  # Un texto bonito y un numero 20

texto = "Un texto {1} y un numero {0}".format(v, n) # Un texto 20 y un numero bonito

print("{num},{num},{num}".format(num=n))  # 20,20,20

print("{:>30}".format("palabra"))  #                        palabra

