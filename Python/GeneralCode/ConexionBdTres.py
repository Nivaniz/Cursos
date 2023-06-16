import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

# Autoincrementable
'''
cursor.execute(
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) NOT NULL,
        marca VARCHAR(50) NOT NULL,
        precio FLOAT NOT NULL)
    )


productos = [
    ('Ritz', 'Whole Foods', 59),
    ('Lala', 'Whole Foods', 29),
    ('Danonino', 'Whole Foods', 39),
    ('Gerber', 'Whole Foods', 19)
]

# Null por ser AI
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
'''

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(producto)

conexion.commit()
conexion.close()