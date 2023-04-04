from collections import Counter, defaultdict, OrderedDict, namedtuple
import datetime
import math
import random

# Contadores
l = [1,2,2,3,4,4,5,4,6,7]
p = "Palabra"
animales = " perro gato canaio perro gato gato gato"

# Transformamos a contador para que nos diga cuantos numeros de cada uno hay

print(Counter(l))
print(Counter(p))  # Counter({'a': 3, 'P': 1, 'l': 1, 'b': 1, 'r': 1})
c = Counter(animales.split())  # Para separarlos

print(c.most_common(2))  # Los dos más comunes

li = [2,2,3,4,4,5,4,20,20,80,80,10,20,30,30]

co = Counter(li)  # para contarlo
print(co.items())  # para separarlos por tuplas [(2, 2), (3, 1), (4, 3), (5, 1), (20, 3), (80, 2), (10, 1), (30, 2)]

c.keys()  # para conseguir los primeros valores como (2, 3, 4, 5....)
c.values()  # para conseguir los segundos valores ( 2, 1, 3, 1)

# Diccionarios por defecto

d = defaultdict(float)
print(d['algo'])  # 0.0 aún sin tener algo en el diccionario

# Diccionarios ordenados

n = OrderedDict()
n['uno'] = 'one'
n['dos'] = 'two'
n['tres'] = 'three'

print(n)

# Tuplas con nombres
Persona = namedtuple('Persona', 'nombre apellido edad')
p = Persona(nombre= 'Exc', apellido='Cos', edad=23)

print(p.nombre)
print(p.apellido)

# DATETIME
dt = datetime.datetime.now()  # Nos muestra la fecha de hoy
print(dt)
dt.year  # 2003
dt.microsecond

dt.isoformat()


# Math
pi = 3.14159
print(round(pi))   # 3

math.floor(pi)  # redondear a la baja
r = math.floor(3.5) # redondear a la baja
print(r)

abs(-10)  # 10
num = [1, 2, 3]
math.fsum(num)  # para floats

print(math.trunc(100.9833833))  # 100

# Random
print(random.random())  #numero al azar mayor que cero y menor que 1

print(random.uniform(1,100))  # entre el uno y el 100

print(random.randrange(100))  # int

# Elegir una letra aleatoria
commm = "Hola mundo"
print(random.choice(commm))