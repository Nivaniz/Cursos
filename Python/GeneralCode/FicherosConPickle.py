# guardar estructuras mas complejas de ficheros
import pickle

lista = [1, 2, 3, 4, 5]
fichero = open('lista.pckl', 'wb')  # Lo abrimos en escritura

pickle.dump(lista, fichero)
# Corta lo que hay en el fichero y pone
# lo que nosotros queremos y en donde
fichero.close()

fichero = open('lista.pckl', 'rb')  # Lectura binaria
lista = pickle.load(fichero)  # Cargamos el fichero
print(lista)  # Contenido recuperado
fichero.close()

# Ejemplo con lista
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

nombres = ['Héctor', 'Mario', 'Marta']
personas = []

for n in nombres:  # Iteramos en los nombres
    p = Persona(n)  # Tomamos la persona y la guardamos en la clase
    personas.append(p)  # Agregamos el nombre de la persona a la variable Personas

fichero = open('personas.pclk', 'wb')
pickle.dump(personas, fichero)
fichero.close()

fichero = open('personas.pclk', 'rb')  # Lectura binaria
people = pickle.load(fichero)  # Cargamos el fichero

for p in personas:
    print(p.nombre)