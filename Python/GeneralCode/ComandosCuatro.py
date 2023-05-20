# For Loops
for item in 'Python':  # Iterar en el string que llamamos item
    print(item)

for item in ['Mosh', 'John', 'Sara']:  # Mostrar lista
    print(item)

for item in range(5, 10):  # 5,6,7,8,9
    print(item)

for item in range(5, 10, 2):  # 5,7,9
    print(item)

prices = [10, 20, 30, 40, 50]
total = 0

for item in prices:
    total = total + item  # Total lo guarda por cada repetición entonces se suma
print(f"Total: {total}")

# Nested Loops
for x in range(4):  # (0,4), (0), (0), (0), (0)
    for y in range(3):  # (0,3), (0) , (1), (2)
        print(f"({x}), ({y})")

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:  # TOMAMOS 5 EN X-COUNT
    output = ''
    for count in range(x_count):  # de 0 a x_count que será 5 y se reperirá 5 veces
        output += 'x'  # Se guardan 0,1,2,3,4 equis(x)
    print(output)  # Da xxxxx

# Listas
names = ['Mosh', 'John', 'Sara']
print(names[2])
names[0] = 'Pepe'
print(names)

numbers_2 = [5, 2, 1, 9, 3, 11, 19]  # Encontrar el número menor
maxim = numbers_2[0]

for x in numbers_2:
    if x > maxim:
        maxim = x
print(maxim)

# 2D listas
# [
#    1 2 3
#    4 5 6
#    7 8 9
# ]
# 3X3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 6, 9],
]

# Acceder a un número individual
matrix[0][1] = 20  # Si quisieramos cambiarlo
print(matrix[0][1])  # Index del 2 de la fila 0

# Para iterar
for row in matrix:
    for item in row:
        print(item)  # obtener todos los elementos

# Metodos de un list
numeros = [5, 2, 1, 7, 4]
numeros.append(20)  # [5, 2, 1, 7, 4, 20]
numeros.insert(0, 20)  # [20, 5, 2, 1, 7, 4]
numeros.remove(5)  # [2, 1, 7, 4]
numeros.clear()  # []
# numeros.index(5)  # 0
50 in numeros  # False

# Puedes guardar una copia de la lista
numeros_2 = numbers.copy()