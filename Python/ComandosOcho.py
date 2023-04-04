# Generando valores random con modulos de python 3 con modules documentation
import random

for i in range(3):
    print(random.random())  # genera un valor random de 0 a 1

for z in range(3):
    print(random.randint(10, 20))  # genera un valor random de dos números asignados

members = ['John', 'Mary', 'Bob']
leader = random.choice(members)  # Elegir un miembro al azar
print(leader)


# Definir una clase llamada Dice
# Definir un método lamado roll que cada que lo escribamos nos de una tupla
#  (2,3)

class Dice:
    def roll(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return f"({x},{y})"


randm1 = Dice()
print(randm1.roll())