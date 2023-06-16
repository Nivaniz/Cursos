# Función lambda y funciones anónimas
"""
def doblar(num):
    resultado = num * 2
    return resultado
print(doblar(5))

AÚN MÁS SIMPLIFICADO
def doblar(num): return num * 2
print(doblar(5))
"""

doblar = lambda num: num * 2
print(doblar(2))

impar = lambda num: num%2 !=0
print(impar(5))

revetir = lambda cadena: cadena[::-1]
print(revetir("Pepe plomero"))

# Función filter
numeros = [2, 5, 50, 33, 23, 33, 15]


def multiple(numero):
    if numero % 5 == 0:
        return True


# list(filter(multiple, numeros))
f = filter(multiple, numeros)  # Permite que sea iterable
print(next(f))  # 5
print(next(f))  # 50

print("________________________")
# Lo mismo de arriba pero más simple
print(list(filter(lambda numero: numero % 5 == 0, sorted(numeros))))  # [5, 50, 15]

# Filtrar dada una lista de personas una de menor edad
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} de {} años".format(self.nombre, self.edad)


personas = [
    Persona("Juan", 35),
    Persona("Pepe", 25),
    Persona("José", 37),
    Persona("Martín", 19)
]

menores = filter(lambda people: people.edad < 35, personas)
for menor in menores:
    print(menor)

'''
Pepe de 25 años
Martín de 19 años
'''

# incrementar edad de cada persona
print("________________________")
personas = list(map(lambda persona: Persona(persona.nombre, persona.edad+1), personas))
for persona in personas:
    print(persona)
print("________________________")
# Función map

numbers = [2, 5, 23, 50, 22, 33]
a = [12, 5, 2, 5, 24, 8]
b = [2, 4, 3, 5, 22, 14]

def double(number):
    return number*2


m = map(double, numbers)  # Con esto se puede iterar
print(list(m))  # [4, 10, 46, 100, 44, 66]

'''
print(next(m))  # 4
print(next(m))  # 10
'''

# O de una manera más sencilla
print(list( map( lambda x: x*2, numbers)))  # [4, 10, 46, 100, 44, 66]
print(list( map( lambda x, y: x*y, a, b)))  # [24, 20, 6, 25, 528, 112]



