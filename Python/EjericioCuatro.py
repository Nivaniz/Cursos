class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: {}, Ruedas: {}".format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad=None, cilindrada=None):
        super().__init__(color,
                         ruedas)  # Utilizamos super() sin self en lugar del vehiculo para llamar atributos externos
        # Mencionamos los nuevos atributos
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", Velocidad: {}, Cilindraje: {}".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):  # Camioneta hereda de coche
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", Carga: {}".format(self.carga)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: {}".format(self.tipo)


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", Velocidad: {}, Cilindraje: {}".format(self.velocidad, self.cilindrada)


def catalogar(vehicles):
    for v in vehicles:
        print(type(v).__name__, v)  # Type imprime el nombre de la clase, y el, v y imprime una representación del
        # objeto (sus datos de esa __str__)


def catalogacion(vehicles, ruedas=None):  # Buscar elementos con ruedas
    if ruedas is not None:
        contador = 0
        for v in vehicles:
            if v.ruedas == ruedas:
                contador += 1
        print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))

    for v in vehicles:
        if ruedas is None:
            print(type(v).__name__, v)  # Mostramos todos los elementos de la lista
        else:
            if v.ruedas == ruedas:  # si el numero de ruedas del vehiculo es igual al num de ruedas que pasamos como argumento
                print(type(v).__name__, v)


# Intanciamos el objeto
vehi = Vehiculo('Rojo', 8)

print("_________________________________________________________________")

car = Coche('Azul', 4, 50, 3)

print("_________________________________________________________________")
truck = Camioneta('Verde', 6, '200', 5, 150)

print("_________________________________________________________________")
bicicle = Bicicleta('Amarillo', 2, 'Urbana')

print("_________________________________________________________________")
motocicle = Motocicleta('Negra', 2, 'Mortalika', 250, 8)

print("_____________________Imprimimos_________________________")

vehicles = [vehi, car, truck, bicicle, motocicle]

print("______________________A_________________________")
catalogar(vehicles)
print("__________________________B_________________________")
catalogacion(vehicles, 2)  # Imprime los que tienen ese tipo de ruedas

