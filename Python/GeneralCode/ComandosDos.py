import math

# Librería fundamental de métodos

# Operadores Aritmeticos
x = 10
x = x + 3  # Es lo mismo que 13
x += 3  # Da 16
x -= 4  # Da 12
print(x)

# Funciones matemáticas
# Podemos encontrar la documentacion y su explicación como python 3 math module
y = 2.9
print(round(y))  # 3
print(abs(-2.9))  # Siempre regresa un numero positivo
print(math.ceil(2.9))  # 3
print(math.floor(2.9))  # 2

# If
is_hot = False
is_cold = True

if is_hot:
    print("Es un día caliente")
    print("Bebe agua")
elif is_cold:
    print("Es un día frio")
    print("Abrigate")
else:
    print("Disfruta tu día")

price = 1000000
good_credit = True

if good_credit:
    discount = 0.1 * price
else:
    discount = 0.2 * price
print(f"El precio final de la casa es de ${discount}")

# Operadores logicos
# NOT, OR AND
has_high_income = True
has_good_credit = True

# if has_high_income and has_good_credit:  # Si ambos son true corre la linea si uno es falso no la corre
# print("Puede aplicar para una deuda")

# if has_high_income or has_good_credit:  # Si una es verdadera funciona, si ambas son falso no funciona
# print("Puede aplicar para una deuda")

temperature = 30

if temperature == 30:
    print("Es un día caliente")
else:
    print("No es un día caliente")

name = input('What is your name? ')

if len(name) < 3:
    print("Name must be al least 3 characters")
elif len(name) > 10:
    print("Name must be al least min 10 characters")
else:
    print("Name i´ts good")

# Convertidor de pesos
weight = int(input('Weight: '))
libra_Kilo = input('(L)bs or (K)g')

if libra_Kilo.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif libra_Kilo.upper() == 'K':
    converted = weight / 0.45  # / tenemos float con // tenemos integer
    print(f"You are {converted} pounds")
else:
    print("You are putting something wrong")