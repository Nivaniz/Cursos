import pandas as pd
import numpy as np

# Rango de fechas para usar de índice en un dataframe
index = pd.date_range("7/15/2023", periods=20)

print(index)

# Lo utilizamos para rellenar un df con valores aleatorios
df = pd.DataFrame(np.random.randn(20, 4), index=index, columns=["A", "B", "C", "D"])

print("_________")
print(df)
'''
# Devuelve las primeras 5
df.head()
# Primeras tres filas
df.head(3)
# Últimas tres filas
df.tail(3)
'''
print("_________")
df = pd.DataFrame({
    'enteros': [100, 200, 300, 400],
    'decimales': [3.14, 2.72, 1.618, 3.14],
    'cadenas': ['hola', 'adiós', 'hola', 'adiós']})

print(df)
'''
   enteros  decimales cadenas
0      100      3.140    hola
1      200      2.720   adiós
2      300      1.618    hola
3      400      3.140   adiós
'''

