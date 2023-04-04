from io import open
import pickle


class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre, self.vida, self.ataque,
                                                                         self.defensa, self.alcance)


class Gestor:
    personajes = []

    # Constructor de clase
    def __init__(self):
        # Cargar las películas del fichero
        self.cargar()

    def agregar(self, p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:  # Recorremos todos los perosnajes
                return
        self.personajes.append(p)
        self.guardar()  # Para guardarlas en el fichero

    def borrar(self, nombre):
        for pTemp in self.personajes:
            if pTemp.nombre == nombre:  # Recorremos todos los perosnajes
                self.personajes.remove(pTemp)  # para borar el que se parece
                self.guardar()  # Para guardarlas en el fichero
                return "Personaje {} borrado".format(nombre)

    def mostrar(self):
        if len(self.personajes) == 0:
            print("El personaje no existe")
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('Personas.pckl', 'ab+')  # Append binario con funciones de lectura
        fichero.seek(0)  # Ya que va a cargar varias veces tenemos que regresar el puntero

        # Buscamos si hay películas
        try:
            self.personajes = pickle.load(fichero)  # Se cargan y leen datos al fichero
        except:
            pass
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))

    def guardar(self):
        fichero = open('Personas.pckl', 'wb')
        pickle.dump(self.personajes, fichero)  # guarda un objeto serializado de Python self.peliculas
        fichero.close()


# Crear el personaje

G = Gestor()

'''
G.mostrar()

G.agregar(Personaje("Caballero", 4, 2, 4, 2))
G.agregar(Personaje("Guerrero", 2, 4, 2, 4))
G.agregar(Personaje("Arquero", 2, 4, 1, 8))
print("______________________________________")
G.mostrar()
'''

G.borrar("Arquero")
G.mostrar()