# Filas separadas por comas
import csv

# Lista con tuplas
contactos = [
    ('Marie', 'UX', 'marie@gmail.com'),
    ('Javier', 'UI', 'javier@gmail.com'),
    ('Pepe', 'SOF', 'pepe@gmail.com')
]

# Permite abrir un fichero en un bloque
# de código sin cerrarlo manualmente
with open("contactos.csv", "w", newline="\n") as csvfile:  # el newline es para
    # especificar el tipo de salto de línea entre las filas y al final la variable donde se va guardar
    writer = csv.writer(csvfile, delimiter=",")  # El archivo más delimitador
    # Si fuese un diccionario se usa DictWriter()
    for contacto in contactos:
        writer.writerow(contacto)

# Para guardarlo y que se guarde cada nombre en el archivo

# Para leer la información:
with open("contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",") # Si fuese un diccionario se usa fieldname
    for nombre, empleo, email in reader:
        print(nombre, empleo, email)