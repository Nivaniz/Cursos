import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Podemos crear un arreglo a partir de
array = np.array([1, 2, 3, 4, 5])

# Y lo mostramos
print(array)

# Para ver su dimensión (1) [1 2 3 4 5]
print(array.ndim)

# Para ver su forma (5, ) cinco elementos en la primera fila
print(array.shape)

arreglo = np.array(
    [
        [1, 2, 3, 4, 5],
        [7, 8, 4, 4, 5]
    ]
)

print(arreglo.ndim)  # 2 ancho y alto
print(arreglo.shape)  # (2,5) dos filas y cinco columnas

# Tabla Y Gráficos
tabla = pd.DataFrame(
    np.random.randint(0, 200, size=(4, 3)),  # Generar numeros random de 0-200 en forma 4x
    columns=['Pepe', 'María', 'Juan']
)

print(tabla)

tabla.plot()
plt.show()  # Para que aparezca la tabla de forma gráfica

