# Bucles anidados

lista = ["Hola", 10, "Adiós", [20, 10, 150]]
print(lista[-1])  # [20, 10, 150]

print(lista[-1][0])  # [20]

for numero in lista[-1]:
    print(numero)  # 20,10,150

new_list = [
    "This is a text",  # Cadena
    (1, 5, 15, 20, 25),  # Tupla
    ["Azul", "Verde", "Amarillo"]  # Lista
]

print(new_list)  # HORIZONTAL

for colection in new_list:
    print(colection)  # VERTICAL

for colection in new_list:
    for elemento in colection:
        print(colection)
        print(elemento)

tabla = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]

for fila in tabla:
    for columna in fila:
        print(columna, end=" ")  # 0 0 0 1 1 1 2 2 2
    print()

# CUBO
new_table = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]

# CONJUNTOS ( no puede haber elementos duplicados )

conjunto = set()
conjunto = {1, 2, 3}

conjunto.add(4)  # {1, 2, 3, 4}
conjunto.add(0)  # {0, 1, 2, 3, 4}
conjunto.add('H')  # {0, 1, 2, 3, 4, 'H'}
conjunto.add('A')
conjunto.add('Z')  # {0, 1, 2, 3, 4, 'A', 'Z', 'H'}

# Para saber si una persona está dentro del grupo
grupo = {'Miguel', 'Juan', 'Sam'}

print('Miguel' in grupo)  # True

l = [1, 1, 2, 3, 4, 5, 5, 5]

c = set(l)
print(c)  # {1,2,3,4,5}

l = list(c)
print(l)  # [1,2,3]

# l = list( set(l))

