import json
from helpers import absPath  # Importa la función absPath desde el módulo helpers

datos = []

# Agrega un contacto a la lista de datos
datos.append({
    "Nombres": "Samuel David",
    "Apellidos": "Serrato Loyola",
    "Edad": "20",
    "Empleo": "Estudiante",
    "Email": "Samuel@gmail.com"
})

# Crea una lista de tuplas de contactos
contactos = [
    ("Maria Nadia", "Guerrero Martinez", "50", "Costurera", "Maria@gmail.com"),
    ("Juan Perez", "Garcia Melendez", "35", "Arquitecto", "juanperez@email.com"),
    ("Ana Rodriguez", "Lopez Lopez", "28", "Abogada", "anarodriguez@email.com"),
    ("Luis Sanchez", "Mendoza Gonzalez", "42", "Chef", "luissanchez@email.com")
]

# Convierte las tuplas de contactos en diccionarios y los agrega a la lista de datos
for nombres, apellidos, edad, empleo, email in contactos:
    datos.append({
        "Nombres": nombres,
        "Apellidos": apellidos,
        "Edad": edad,
        "Empleo": empleo,
        "Email": email
    })

# Escribe la lista de datos en un archivo JSON
with open(absPath("contactos.json"), "w") as archivo:
    json.dump(datos, archivo)

datos = None  # Limpia la variable datos

# Lee los datos del archivo JSON y los imprime en la consola
with open(absPath("contactos.json")) as archivo:
    datos = json.load(archivo)
    for contacto in datos:
        print(contacto["Nombres"], contacto["Apellidos"], contacto["Edad"], contacto["Empleo"], contacto["Email"])
