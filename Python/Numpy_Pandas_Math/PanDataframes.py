import numpy as np
import pandas as pd

# Asignación de serie unida mediante índices
array = np.random.uniform(-10, 10, size=[4,4])
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])
print(df)

'''
          W         X         Y         Z
A  9.806738 -2.197888  5.718496 -4.620127
B -5.662729 -3.306869  6.288822 -3.946447
C  5.552027 -1.156915 -8.700502 -4.716711
D  0.536320 -9.096799  3.412085  7.666985
'''

# Consultar una de las columnas y nos da una serie
print(df['X'])

'''
A   -2.197888
B   -3.306869
C   -1.156915
D    -9.096799
'''

# Consultar varias columnas
print(df[['Y', 'Z']])

'''
          Y         Z
A  0.776709 -4.723629
B  9.376168 -9.079643
C  3.007116  1.931841
D -5.269341  1.772984
'''

# Consultar filas
print(df.loc['C'])  # O podemos usar indices en vez de letras 0,1,2
'''
W   -7.436909
X   -1.756337
Y   -6.313565
Z   -4.740506
'''

# Añadir una columna
df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df)

'''
          W         X         Y         Z     TOTAL
A -1.320618  2.584070 -5.791367  9.679951  5.152037
B  6.480314  4.093159 -3.337003 -8.763651 -1.527181
C  3.294130  9.745676 -4.099330 -2.859921  6.080554
D -2.246743  9.441137  7.460250 -8.956898  5.697747
'''

# Añadir una fila
df.loc[len(df)] = [1, 2, 3, 4, 10]
print(df)

'''
          W         X         Y         Z      TOTAL
A -8.407647 -3.348005 -6.913563 -8.056898 -26.726113
B  8.978663  4.037631  8.441147  0.666495  22.123935
C  4.725696 -2.925682  7.320046 -7.594242   1.525818
D  2.457582 -2.926099  5.608360 -9.497952  -4.358109
4  1.000000  2.000000  3.000000  4.000000  10.000000
'''

# Borrar una columna
# df.drop('TOTAL', axis=1) pero no se modifica el df original para eso hacemos:
# df.drop('TOTAL', axis=1, inplace=True)

# Borrar una fila df.drop('D', axis=0)

# Seleccionar una fila y columna específica:
# Fila C columna Z
print(df.loc['C', 'Z'])
# -8.894299521351057

'''
# Filas A,B y columnas W,Y
df.loc[['A','B'],['W','Y']]
'''

# Dataframe mayor que cero
print(df>0)

'''
       W      X      Y      Z  TOTAL
A   True   True  False   True   True
B  False  False   True   True  False
C   True  False   True   True   True
D   True  False   True  False   True
4   True   True   True   True   True
'''

'''
# Valor de los registros >0
df[df>0]
# Valor de los registros cuando X>0
df[df['X']>0]
# Valor de los registros en las columnas Y,Z si X>0
df[df['X']>0][['Y','Z']]
# Valor de los registros en las columnas W e Y cuando X>0 o Z<0
df[(df['X']>0) | (df['Z'] < 0)][['W','Y']]
'''

print("______MODIFICAS ÍNDICES_________")
# Creamos de nuevo el dataframe
arrayNuevo = np.random.uniform(-10, 10, size=[4,4])
dfNuevo = pd.DataFrame(arrayNuevo, index=['A','B','C','D'], columns=['F','S','T','FO'])

# Añadimos una nueva Serie con el nombre de los índices
dfNuevo['Códigos'] = ['AA','BB','CC','DD']
print(dfNuevo)
'''
          F         S         T        FO Códigos
A  3.318156  7.401372  6.578322 -1.592949      AA
B  4.201400  8.086361  6.211290  8.636837      BB
C -4.147680 -2.842885 -7.019759 -8.294714      CC
D -4.654482  9.966042  3.379129  6.252538      DD
'''

# Substituimos los índices de las filas
dfNuevo.set_index('Códigos', inplace=True)
print(dfNuevo)
'''
                F         S         T        FO
Códigos                                        
AA       3.815712 -2.475645  9.869749  2.540022
BB       0.018310  9.505438 -1.991578 -0.500934
CC      -5.363967  7.750409  0.844038 -0.094866
DD       0.595898  8.344283  2.693035 -6.641597
'''

'''
# Reiniciamos los índices y borramos los anteriores explícitamente
df.reset_index(drop=True, inplace=True)
'''