import sqlite3

conexion = sqlite3.connect("usuariosai.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE usuariosai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100))
    ''')


users = [
    ('11111111A', 'Hector', 29, "hec@gmail.com"),
    ('22222222B', 'Miguel', 59, 'mike@gmail.com'),
    ('33333333C', 'Maria', 18, 'lic@gmail.com'),
    ('44444444D', 'José', 27, 'jose@gmail.com')
]

# Null por ser AI
cursor.executemany("INSERT INTO usuariosai VALUES (null,?,?,?,?)", users)
'''

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
'''

conexion.commit()
conexion.close()