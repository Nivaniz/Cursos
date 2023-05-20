import numpy as np
from colorama import init, Fore, Back, Style

init()  # Inicializar los estilos de colores

arr_2d = np.array(([0, 5, 10], [15, 20, 25], [30, 35, 40]))
print(Fore.YELLOW + str(arr_2d))

"""
[[ 0  5 10]
 [15 20 25]
 [30 35 40]]
"""
print('')

# Primera fila
print(Fore.MAGENTA + str(arr_2d[0]))  # [ 0  5 10]
print('')
# Primera fila y primera columna
print(Fore.CYAN + str(arr_2d[0][0]))  # 0*

# Slycing solo de la primera columna
print(Fore.YELLOW + str(arr_2d[:, :1]))
"""
[[ 0]
 [15]
 [30]]
"""

# Fancy Index
arr_2d_md = np.zeros((5, 10))
print(Fore.BLUE + str(arr_2d_md))
print('')
# Modificamos masivamente la primera, tercera y última fila
arr_2d_md[[0, 2, -1]] = 5
print(arr_2d_md)

""""
[[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]]
"""

# Bucles
for fila in arr_2d:
    print(fila)
"""
[ 0  5 10]
[15 20 25]
[30 35 40]
"""


