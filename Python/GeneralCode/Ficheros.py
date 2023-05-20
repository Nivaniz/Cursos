from io import open

# Abrir ficheros

texto = "Una línea con texto\nOtra línea con texto"

# Guardar en un fichero
# Lo creamos
fichero = open('fichero.txt', 'w')  # Lo abrimos con el modo de escritura

fichero.write(texto)  # Para escribirle nuestras cosas

fichero.close()  # Para cerrarlo

# del fichero  PARA BORRARLO DE LA MEMORIA

# Lo abrimos con el modo LECTURA
fichero = open('fichero.txt', 'r')

texto = fichero.read()

fichero.close()

# Leer las lineas editadas desde el fichero
fichero = open('fichero.txt', 'r')
# lineas = fichero.readlines() # Para leer todas las líneas
# print(lineas[0])  # Una línea con texto

fichero.close()

fichero = open('fichero.txt', 'a')  # Agregar algo al fichero
fichero.write('\nPepeto')

with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)

# Manejar el puntero

print("_______________________")
fichero = open('fichero.txt', 'r')
# Apuntar al caracter numero 10
fichero.seek(10)
a = fichero.read()  # Lee a partir de el caracter 10
print(a)
print("_______________________")
fichero.seek(0)  # Lo mandamos de nuevo al cero
print(fichero.read(5))  # Leer 5 caracteres
print(fichero.read())  # Leer a partir del caracter 5

print("_______________________")
# Leer la mitad del texto
fichero.seek(0)
texto = fichero.read()
fichero.seek(len(texto) / 2)  # Buscamos la mitad del fichero
print(fichero.read()) # Leeemos
fichero.close()

# Lectura y escritura a la vez
# Pone el puntero al principio
fichero = open('fichero.txt', 'r+')  #Lectura y escritura
fichero.write('Línea 299383')
fichero.close()


print("_______________________")
# Modificar una línea especial
fichero = open('fichero.txt', 'r+')
lines = fichero.readlines()
lines[1] = "Esta línea la he modificado en memoria\n"
print(lines)

fichero.seek(0)
fichero.writelines(lines)  # Escribir las líneas ya previamente
