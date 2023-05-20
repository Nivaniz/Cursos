import numpy as np
import pandas as pd

# Definimos un dataframe con datos de ejemplos
df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])

df.to_csv('datos.csv', index=False)

df = pd.read_csv('datos.csv')
print(df)

