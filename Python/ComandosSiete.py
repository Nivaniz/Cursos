# Clases
class Galleta:  # Las clases pueden tener métodos y los métodos atributos
    pass


una_galleta = Galleta()  # Creación de objetos (instanciación)
otra_galleta = Galleta()  # Objeto es una instancia

una_galleta.sabor = "Salado"  # Atributos de la instancia
una_galleta.color = "Marrón"

print(f"El sabor de esta galleta es: {una_galleta.sabor}")  # Salado


class Pastel():
    chocolate = False  # Atributo

    def __init__(self, sabor, color=None, forma=None):  # Funcion especial con atributo que llama al objeto
        # Se puede asignar en los parametros un none para que no sea obligatorio
        self.sabor = sabor
        self.color = color
        self.forma = forma

        if color and forma is not None:
            print("Se acaba de crear un pastel sabor {} color {} con forma {}".format(sabor, color, forma))
        else:
            print("Se acaba de crear un pastel sabor{}".format(sabor))  # SI SE PASA VACÍO

    def chocolatear(self):
        self.chocolate = True  # Atributo cambiado

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy un pastel chocoleatado")
        else:
            print("Soy un pastel sin chocolate")


p = Pastel("dulce", "café", "redonda")
p.tiene_chocolate()
p.chocolatear()  # Cambiando un atributo interno
print(p.chocolate)
p.tiene_chocolate()

# Paquetes
# HOMBRES | MUJERES : SON PAQUETES
# Adentro de hombres hay : ZAPATOS | PLAYERAS -> Son modules
