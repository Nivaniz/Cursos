import sqlite3
from prettytable import PrettyTable

# Crear BD
conexion = sqlite3.connect("ejemplo.db")

# Crear una tabla para almacenar los resultados
tabla = PrettyTable()

# Consulta a la base de datos
cursor = conexion.cursor()

# Ejecutar consulta (crear tabla)
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

# Para insertar registro
#cursor.execute("INSERT INTO usuarios VALUES ('Hector',19,'hector@gmail.com')")

# Ejecucuión masiva
'''usuarios = [
    ('Miguel',59,'mike@gmail.com'),
    ('Maria',18,'lic@gmail.com'),
    ('José',27,'jose@gmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)
'''''

# Para recuperar registros


''''Se está obteniendo los nombres de las columnas de la consulta mediante 
la propiedad description del cursor de la base de datos.

La propiedad description contiene una lista de tuplas, donde cada tupla 
representa una columna de la consulta.'''
# Obtener los nombres de las columnas
nombres_columnas = [d[0] for d in cursor.description]

# Agregar los nombres de las columnas a la tabla
tabla.field_names = nombres_columnas

# usuario = cursor.fetchone()  # Recupere el primer registro en forma de tupla
# print(usuario[0])  # Para acceder unicamente al nombre
# print(usuario) # Para acceder a todos

# Agregar los registros a la tabla
registros = cursor.fetchall()  # Regresa una lista
for registro in registros:
    tabla.add_row(registro)

# Mostrar la tabla en la consola
print(tabla)

# Confirmar cambios
conexion.commit()

conexion.close()