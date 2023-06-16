import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

''''
Creacion de tabla 
cursor.execute(
    CREATE TABLE usuarios (
        dni VARCHAR(9) PRIMARY KEY,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
    ))
'''''

'''''
usuarios = [
    ('11111111A','Hector', 29, "hec@gmail.com"),
    ('22222222B','Miguel', 59, 'mike@gmail.com'),
    ('33333333C','Maria', 18, 'lic@gmail.com'),
    ('44444444D','José', 27, 'jose@gmail.com')
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)
'''''

# Autoincrementable

conexion.commit()
conexion.close()