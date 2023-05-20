import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A':[7, 8, -6, 8],
    'B':[12, np.nan, 1, np.nan],
    'C':[4, np.nan, np.nan, np.nan],
    'D':[4, np.nan, -2, -10]})

print(df)
'''
   A     B    C     D
0  7  12.0  4.0   4.0
1  8   NaN  NaN   NaN
2 -6   1.0  NaN  -2.0
3  8   NaN  NaN -10.0
'''

# Comprobar regitros nulos
print(df.isnull())

'''
       A      B      C      D
0  False  False  False  False
1  False   True   True   True
2  False  False   True  False
3  False   True   True  False
'''

# Descartar filas con registros nulos
print(df.dropna())

'''
   A     B    C    D
0  7  12.0  4.0  4.0
'''

# Descartar columnas con registros nulos
print(df.dropna(axis=1))

'''
   A
0  7
1  8
2 -6
3  8
'''

# Rellenar los registros de las filas vacías con un valor
print(df.fillna(value=0))

'''
   A     B    C     D
0  7  12.0  4.0   4.0
1  8   0.0  0.0   0.0
2 -6   1.0  0.0  -2.0
3  8   0.0  0.0 -10.0
'''
