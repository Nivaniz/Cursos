# Array de ceros
import numpy
import numpy as np

ceros = np.zeros(3)
print(ceros)  # [0. 0. 0.]
print("________________")
# Pero si queremos multidimensionales
ceros_tabla = np.zeros([3, 3])
print(ceros_tabla)

"""
Tabla de unos = np.ones([3, 3])
Tabla de identidad = np.eye(3)
"""
print("________________")

# Array de rangos
# Rango de 0 a 4
cero_tres = np.arange(4)
print(cero_tres)  # [0 1 2 3]

"""
Rango 0 a 4 decimal = np.arange(4.)
Rango de -3 a 4 = np.arange(-3, 3)
Rango de 20 números a partir de 0 cada 5 números = np.arange(0, 20, 5)
"""
