import numpy as np
import pandas as pd

# Creamos un diccionario con mucha información
ventas = {
    'Comercial': ['Juan', 'María', 'Manuel', 'Vanesa', 'Ana', 'Marcos'],
    'Empresa': ['Movistar', 'Jazztel', 'Movistar', 'Jazztel', 'Vodafone', 'Vodafone'],
    'Paga Extra': [300, 220, 140, 70, 400, 175]
}

df = pd.DataFrame(ventas)
print(df)
'''
  Comercial   Empresa  Paga Extra
0      Juan  Movistar         300
1     María   Jazztel         220
2    Manuel  Movistar         140
3    Vanesa   Jazztel          70
4       Ana  Vodafone         400
5    Marcos  Vodafone         175
'''
print("_________")
# Eliminar la columna "Comercial"
df = df.drop('Comercial', axis=1)
por_empresa = df.groupby('Empresa')

# Media por empresa
print(por_empresa.mean())
'''
          Paga Extra
Empresa             
Jazztel        145.0
Movistar       220.0
Vodafone       287.5
'''
print("_________")
# Desviación estándar (dispersion del conjunto)
print(por_empresa.std())
'''
          Paga Extra
Empresa             
Jazztel   106.066017
Movistar  113.137085
Vodafone  159.099026
'''

# Para volver a agregar Comercial
df = df.join(pd.DataFrame(ventas['Comercial'], columns=['Comercial']))
# Usamos el ID de las primas máximas como fuente del df
print(df.loc[por_empresa['Paga Extra'].idxmin()])

'''
    Empresa  Paga Extra Comercial
3   Jazztel          70    Vanesa
2  Movistar         140    Manuel
5  Vodafone         175    Marcos
'''

# Reporte de analíticas descriptivas por empresa
print(por_empresa.describe())

'''
              count   mean         std    min     25%    50%     75%    max
Empresa                                                                    
Jazztel         2.0  145.0  106.066017   70.0  107.50  145.0  182.50  220.0
Movistar        2.0  220.0  113.137085  140.0  180.00  220.0  260.00  300.0
Vodafone        2.0  287.5  159.099026  175.0  231.25  287.5  343.75  400.0
'''

# Para girarlo
print(por_empresa.describe().transpose())
print("____________")

# Reporte transpuesto de una sola empresa
print(por_empresa.describe().transpose()['Movistar'])

'''
Paga Extra  count      2.000000
            mean     220.000000
            std      113.137085
            min      140.000000
            25%      180.000000
            50%      220.000000
            75%      260.000000
            max      300.000000
'''