# Herencia

# SUPERCLASE
class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t{}
DESCRIPCIÓN\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)


class Adorno(Producto):  # Para indicar que es hija del producto ponemos nombre y pass
    pass


class Alimento(Producto):  # Nueva clase con atributos no declarados en init
    productor = ""
    distribuidor = ""

    def __str__(self):  # La volvemos a instanciar para agregar los nuevos atributos
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR {}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t{}
PVP\t{}
DESCRIPCIÓN\t{}
ISBN\t{}
AUTOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)


# Intanciamos el objeto
a = Adorno(2033, 'Vaso Adornado', 5, 'Vaso de pocerlana y marmol')

print("_________________________________________________________________")

# Instanciamos el alimento
al = Alimento(2888, "Botella de Aceite", 5, "250ml")
al.productor = "La Marca"
al.distribuidor = "Distribución S.A DE C.V"

print("_________________________________________________________________")
lib = Libro(8477, 'Things have gotten worse since we last spoke', 45, 'Libro sobre canibalismo')
lib.isbn = '3782BN'
lib.autor = 'UNKOWN'

print("_____________________Imprimimos los 3_________________________")

# Polimorfismo
productos = [a, al]
productos.append(lib)

for p in productos:
    print(p, "\n")

# Para mostrarlos con atributos privados de clases normales
print("Mostrarlos por atributo con atributos generales \n")
for p in productos:
    if isinstance(p, Adorno):  # Comprobar si un objeto {p} es del tipo Adorno
        print(p.referencia, p.nombre)
    elif isinstance(p, Alimento):
        print(p.referencia, p.nombre, p.productor)
    elif isinstance(p, Libro):
        print(p.referencia, p.nombre, p.isbn)

print("\n Eso nos permitira mostrar todas las categorías \n")
# Eso nos permitira mostrar todas las categorías
for p in productos:
    print(p.referencia, p.nombre)


# Podemos crear funciones para manejar los atributos de las instancias
# Mediante polimorfirmo como se ve en el método siguiente ya que
# Recibe objetos de distintas clases y accede al atributo pvp dando por entendido que existe en todos lados
def rebajar_producto(p, rebaja):  # Devuelve un producto con una rebaja en porcentaje de su precio
    # p se pasa por referencia (si se cambia el valor total al original)
    p.pvp = p.pvp - (p.pvp / 100 * rebaja)
    return p


print("\nAlimento modificado sus atributos\n")
alimentoRebajado = rebajar_producto(al, 10)
print(alimentoRebajado)

# COPIAR UN OBJETO QUE QUEREMOS MODIFICAR SIN QUE SE CAMBIE EL ORIGINAL
# import copy
# copia_adorno = copy.copy(adorno) y con este trabajamos


