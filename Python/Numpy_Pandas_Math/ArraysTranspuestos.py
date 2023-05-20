import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

"""
[[1 2 3]
 [4 5 6]]
"""
print('_____________________')
# Sus filas se pasan a columnas y sus columnas en filas
print(arr.T)

"""
[[1 4]
 [2 5]
 [3 6]]
"""
print('_________________')

# Funciones universales
arr1 = np.arange(1, 6)
arr2 = np.array([-3, 7, 3, 13, 0])

print(np.add(arr1, arr2))
'''
np.substract = resta
np.sqrt = raiz
np.power = potencia
np.sign = determinar si son positivos 1 o negativos 0
np + sin (seno), cos (coseno), tan (tangente)
np.maximum = maximo los elementos mayores
np.minimum = minimo
np.equal = iguales
np.greater = mayor que
np.fabs = valor absoluto
np.ceil = redondeo el entero al alza
np.floor = redondeo entero a la baja
np.round = redondear de .50
'''

# Funciones aleatorias
a = np.random.rand()  # número decimal entre 0 y 1
print(a)  # 0.7059582717956745

'''
np.random.rand(4) array 1d de decimales entre 0 y 1
np.random.rand(4,2) array 2d de decimales entre 0 y 1
np.random.uniform(10, size = [2,2,2]) array 3d de decimales entre 0 y N(10)
np.random.radint(0, 10, size=[3, 2]) array de enteros entre 0 y n
'''

arreglouno = np.arange(10)
print(arreglouno)  # [0 1 2 3 4 5 6 7 8 9]

# para desordenar el array
np.random.shuffle(arreglouno)
print(arreglouno) # [1 4 0 6 8 7 9 2 5 3]

print('___________')
b = np.random.permutation(15)  # Generar una secuencia permutada a partir de un numero
print(b)  # [ 3 14  4  7 11  8  1  2  9 13  6  0 12 10  5]

print('___________')
# Filtrado de arrays
arr3 = np.random.randint(0, 10, 40) # de 0 a 10, 40 num aleatorios
print(arr3)

print(np.unique(arr3)) # unicos sin repetir
''''
Preguntar si se encuentra una lista en un array:
np.in1d([-1, 4, 8], arr)
Filtrar a partir de una condicion:
np.where(arr1<0, 0, arr1) los elementos sean menores que cero, lo que vamos a poner a cambio, y en que array
'''

arr_bool = np.array(True, True, True, False)
arr_bool.all()  # Comprobar si todos son True
arr_bool.any()  # Comprobar si al menos un elemento es True
