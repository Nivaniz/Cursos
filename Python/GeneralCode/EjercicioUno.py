class Persona:
    def __init__(self, name):
        self.name = name

    def talk(self):  # Método
        print(f"Hi, I am {self.name}")  # regresa el atributo del objeto actual Persona


samuel = Persona("Samuel Serrato")  # Insanciamos Clase con valores
print(samuel.name)  # imprimimos ese atributo asignado
samuel.talk()  # Instanciamos método

bob = Persona("Bob Smith")  # Cada objeto es una diferente instancia de la clase Persona
bob.talk()


# Inherecia
class Mamifero:

    def __init__(self, nombre):
        self.nombre = nombre

    def camina(self):
        print(f"Caminando está {self.nombre}")


class Perro(Mamifero):  # Inherancia de todos los métodos de la clase principal
    pass  # Es un no te preocupes para no tener métodos necesariamente


class Gato(Mamifero):
    def maullar(self):
        print("Meoooow")


perro1 = Perro("Pepe")
perro1.camina()

gato1 = Gato("Roberta")
gato1.camina()
gato1.maullar()
