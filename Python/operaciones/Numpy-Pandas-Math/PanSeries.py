import numpy as np
import pandas as pd

# Serie es un array de numpy, pero con información en los ejes
# Podemos crearlas a partir de una lista, array o diccionario
etiquetas = ['A', 'B', 'C', 'D']
lista = [25, 50, 75, 100]

print(lista)

# serie básica
print(pd.Series(data=lista))
'''
0     25
1     50
2     75
3    100
'''

print("------------")

# serie con etiquetas
print(pd.Series(data=lista, index=etiquetas))

'''
A     25
B     50
C     75
D    100
'''

# parámetros por posición lo mismo que lo de arriba
pd.Series(lista, etiquetas)

print("------------")
# Series on arrays
array = np.random.randint(50, size=4)
print(array)

print(pd.Series(array, etiquetas))

'''
[ 8 33  6 32]
A     8
B    33
C     6
D    32
'''

# Con diccionarios
diccionario = {'A': 25, 'B': 50, 'C': 75, 'D': 100}
print(pd.Series(diccionario))
'''
A     25
B     50
C     75
D    100
'''

# INGRESOS POR ÍNDICES
ingresos = pd.Series([100, 300, 200], index=['enero', 'febrero', 'marzo'])
# acceso por nombre
print("El ingreso de el mes de Enero es: " + str(ingresos['enero']))
#  El ingreso de el mes de Enero es: 100
gastos = pd.Series([100, 150, 250], index=['enero', 'febrero', 'marzo'])
total = ingresos.subtract(gastos)
print("El total es: " + str(total))

'''
El total es: enero 0
febrero  150
marzo  -50
'''