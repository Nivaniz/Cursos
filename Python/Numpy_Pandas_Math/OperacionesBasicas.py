# SUMA
import numpy as np

arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([5, 6, 7, 8])

print(arr_1 + arr_2)  # Si no tiene la misma forma no podemos sumarlos [ 6  8 10 12]
"""
Resta = print(arr_1 - arr_2)
Multiplication = print(arr_1 * arr_2) deben ser las mismas dimensiones de columnas
O multiplicar por un numero  = arr_1 * 10
División = print(arr_1 / arr_2) o  print(arr_1/2)
Inverso = 1 / arr_1
Potencia ==  print(arr_1 ** arr_2)
"""

# Gestion de Arrays
arr_3 = np.arange(0, 50, 5)
print(arr_3)  # [ 0  5 10 15 20 25 30 35 40 45]

print(arr_3[1])  # 5
print(arr_3[-1])  # 45
# Asignacion de un valor
arr_3[-1] = 4
print(arr_3)  # [ 0  5 10 15 20 25 30 35 40  4]

print("________________")

# Slicing
sub_arr = arr_3[:].copy()  # Copia completa
# print(arr_3[:3])  Subarray de los primeros 3 elementos [ 0  5 10]
sub_arr[1:3] = 99
print(sub_arr)  # [ 0 99 99 15 20 25 30 35 40  4]
print(arr_3)  # [ 0  5 10 15 20 25 30 35 40  4]


