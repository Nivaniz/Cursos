from io import open

fichero = open('Personas.txt', 'r', encoding="utf-8")
lineas = fichero.readlines()  # Leemos lo que hay dentro
fichero.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n","").split(";")  # Para borrar el \n lo replace por la nada
    persona = { "Id": campos[0], "Nombre": campos[1], "Apellido": campos[2], "Nacimiento": campos[3], }  # diccionario de la persona
    # La agregamos al diccionario general
    personas.append(persona)

for p in personas:
    print("Id: {} \nNombre: {} {} \nNacimiento: {}".format(p['Id'], p['Nombre'], p['Apellido'], p['Nacimiento']))

''' RESULTADO:
Id: 1 
Nombre: Carlos Pérez 
Nacimiento: 05/01/1989
Id: 2 
Nombre: Manuel Heredia 
Nacimiento: 26/12/1973
Id: 3 
Nombre: Rosa Campos 
Nacimiento: 12/06/1961
Id: 4 
Nombre: David García 
Nacimiento: 25/07/2006
'''