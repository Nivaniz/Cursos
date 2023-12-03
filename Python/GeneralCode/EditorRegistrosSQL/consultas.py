import sys
from helpers import absPath
from PySide6.QtSql import QSqlDatabase, QSqlQuery

conexion = QSqlDatabase.addDatabase("QSQLITE")
conexion.setDatabaseName(absPath("Contactos.db"))

if not conexion.open():
    print("No se puede conectar a la Base de Datos")
    sys.exit(True)

consulta = QSqlQuery()
consulta.exec("DROP TABLE IF EXISTS contactos")
consulta.exec("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nombres VARCHAR(50) NOT NULL,
        apellidos VARCHAR(50) NOT NULL,
        sexo CHAR(1),
        edad DECIMAL NOT NULL,
        empleo VARCHAR(50),
        numero VARCHAR(20) UNIQUE NOT NULL,
        email VARCHAR(40) UNIQUE NOT NULL
    )""")

# Ejecución de consultas dinámicas: formato de cadena
nombres, apellidos, sexo, edad, empleo, numero, email = "Samuel David", "Serrato Loyola", "M", "20", "Programador", "442-186-9547","samuel@gmail.com"

consulta.exec(f"""
    INSERT INTO contactos (nombres, apellidos, sexo, edad, empleo, numero, email)
    VALUES ('{nombres}', '{apellidos}', '{sexo}', '{edad}','{empleo}', '{numero}', '{email}')""")


contactos = [
    ("Maria Nadia", "Guerrero Martinez", "F", "50", "Costurera", "442-186-9747", "Maria@gmail.com"),
    ("Juan Perez", "Garcia Melendez", "M", "35", "Arquitecto", "442-186-9047", "juanperez@email.com"),
    ("Ana Rodriguez", "Lopez Lopez","F", "28", "Abogada", "442-186-9577", "anarodriguez@email.com"),
    ("Luis Sanchez", "Mendoza Gonzalez", "M", "42", "Chef", "442-186-9347", "luissanchez@email.com")
]

consulta = QSqlQuery()
consulta.prepare("""
    INSERT INTO contactos (nombres, apellidos, sexo, edad, empleo, numero, email) VALUES (?, ?, ?, ?, ?, ?, ?)""")

for nombres, apellidos, sexo, edad, empleo, numero, email in contactos:
    consulta.addBindValue(nombres)
    consulta.addBindValue(apellidos)
    consulta.addBindValue(sexo)
    consulta.addBindValue(edad)
    consulta.addBindValue(empleo)
    consulta.addBindValue(numero)
    consulta.addBindValue(email)
    consulta.exec()  # Aquí ejecutas la consulta preparada

# Consultar registros
consulta.exec("SELECT nombres, apellidos, sexo, edad, empleo, numero, email FROM contactos")

# ponemos el cursor en el primer registro
if consulta.first():
    print(consulta.value("nombres"),
          consulta.value("apellidos"),
          consulta.value("sexo"),
          consulta.value("edad"),
          consulta.value("empleo"),
          consulta.value("numero"),
          consulta.value("email"))

# Automatizmaos el cursor hasta el final
while consulta.next():
    print(consulta.value("nombres"),
          consulta.value("apellidos"),
          consulta.value("sexo"),
          consulta.value("edad"),
          consulta.value("empleo"),
          consulta.value("numero"),
          consulta.value("email"))


# Cerrar conexión a la base de datos
conexion.close()
print("Conexion cerrada", not conexion.isOpen())
