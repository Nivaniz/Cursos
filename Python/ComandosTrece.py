# Métodos especiales
class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película", self.titulo)

    # Destructor de clase
    # def __del__(self):
    #  print("Se está borrando la película", self.titulo)

    # Redefinimos el método string
    def __str__(self):  # Para conseguir info de los objetos creados en la memoria
        return "{} lanzada en {} con una duracion de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    # Redefinimos el método en
    def __len__(self):
        return self.duracion


# Si ponemos del(p) nos diría que se está borrando la pelicula

pe = Pelicula("El padrino", 175, 1972)
print(str(pe))
print(len(pe))  # 175

print("___________________________________________")


# Objetos dentro de objetos
class Movie:
    # Constructor de clase
    def __init__(self, title, duration, released):
        self.title = title
        self.duration = duration
        self.released = released
        print("Se ha creado la película", self.title)

    def __str__(self):  # Para conseguir info de los objetos creados en la memoria
        return "{} lanzada en ({})".format(self.title, self.released)


class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    # Método interno para agregar películas manualmente

    def agregar(self, p):
        self.peliculas.append(p)  # Agregamos pelicula a la lista

    # Mostrar película
    def mostrar(self):
        for p in self.peliculas:
            print(p)


p = Movie("El padrino", 175, 1972)
c = Catalogo([p])  # Le pasamos película

c.mostrar()  # El padrino lanzada en 1972

c.agregar(Movie("Elsa", 198, 2010))  # Agregamos al catalogo
c.mostrar()


# Encapsulacion de atributos y métodos
class Ejemplo:
    __atributo_privado = "SOY UN ATRIBUTO INALCANZABLE"  # Attribute privacy

    def __metodo_privado(self):
        print("soy un método inalcanzable")

    def atributo_publico(self):
        return self.__atributo_privado  # Atributo público
        # o si quisieramos devolver el método privado:
        # return self.__metodo_privado()


e = Ejemplo()
print(e.atributo_publico()) # Acceso a un atributo a traves de un método
# e.metodo_publico() Acceso a un método privado a traves de un método público
# print(e.__atributo_privado) no dejara pq es privado


# Método self
class Test:
    contador = 0  # Atributo de clase

    def __init__(self):
        Test.contador += 1
        print(f"Instancias de Test creadas -> {Test.contador}")


for i in range(10):
    Test()  # Instanciamos la clase 1,2,3,4,5,6,...10

