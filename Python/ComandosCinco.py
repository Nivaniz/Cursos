lista = [2, 2, 3, 5, 6, 7, 7]
lista_nueva = []

for item in lista:  # Por cada lista
    if item not in lista_nueva:  # Por cada numero si el numero agregado ni está
        lista_nueva.append(item)  # agregarlo

print(lista_nueva)

# Tuplas (no podemos cambiarlos ni modificarlos)
numbers = (1, 2, 3)
print(numbers[1])

# Unpacking
cordenadas = (1, 2, 3)  # x,y,z

# x = cordenadas[0]
# y = cordenadas[1]
# z = cordenadas[2]

x, y, z = cordenadas  # Es lo mismo que lo de arriba
print(z)  # 3

# Diccionarios
# Key: Name Value: John Smith
customer = {
    "Name: ": "John Smith",
    "Age: ": 30,
    "is_verified": True,
}

customer["Name: "]  # Regresa el valor asociado a la key name
customer["Name: "] = "Jack"  # Cambia el valor de la key
customer.get("birthdate", "Jan 2003")  # Si no existe ese valor cambiarlo a otro asignado

for n, d in customer.items():
    print(n, d)
# "Name: ": "John Smith",
#  "Age: ": 30,
#  "is_verified": True

# FORMA 1
phone = input("Phone: ")  # Si metes un numero te sale los numeros en letra
new_list = []

for num in phone:  # Por cada lista
    if int(num) == 1:
        print("One")
    elif int(num) == 2:
        print("Two")
    elif int(num) == 3:
        print("Three")
    elif int(num) == 4:
        print("Four")
    elif int(num) == 5:
        print("Five")
    elif int(num) == 6:
        print("Six")
    elif int(num) == 7:
        print("Seven")
    elif int(num) == 8:
        print("Eight")
    elif int(num) == 9:
        print("Nine")
    elif int(num) == 0:
        print("Cero")

# FORMA 2
phone_new = input("Phone: ")
diggits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
}

output = ""
for character in phone_new:  # Recorrer lista
    output += diggits.get(character, "#") + " "
# diggits toma el diccionario y get busca si el número primero,segundo... está en el diccionario y lo guarda en output
print(output)

message = input(">")
words = message.split(' ')  # Si lo imprimimos imprime en lista cada mensaje separado
emojis = {
    ":)": "😀",
    ":(": "😞",
}

output = ""
for word in words:
    output += emojis.get(word, word) + ""  # Si no está el emoji imprime directamente la palabra ingresada
print(output)
