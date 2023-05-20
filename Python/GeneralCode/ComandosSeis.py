# Funciones

def greet_user():
    print("Hi")
    print("Welcome")


print("start")
greet_user()
print("Finish")


# Parametros
def greet_user_two(name):
    print("Hi " + name)
    print("Welcome")


print("start")
greet_user_two("John")  # Parametro es name argumento es john
greet_user_two("Mary")  # Reutilizando
print("Finish")


# Argumentos de keyword
# Si queremos que algun argumento vaya en un orden especifico


def greet_user_three(first_name, last_name):
    print(f"Hi {first_name}{last_name}")
    print("Welcome")


print("start")
greet_user_three(last_name="Smith", first_name="John")  # Parametro es name argumento es john
print("Finish")


# Return
def square(number):
    return number * number  # El cuadrado de un número


# Return lo guarda y así lo podemos guardar en una variable

print(square(3000))  # PODEMOS PASAR LA FUNCION QUE DA UN VALOR Y QUE PASAMOS COMO UN ARGUMENTO


# Varios tipos de datos
def test():
    return 'Una cadena', 20, [1, 2, 3]


c, n, l = test()
print(c)  # 'Una cadena'
print(n)  # 20
print(l)  # [1, 2, 3]

# Funcion rehusable
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😞",
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + ""  # Si no está el emoji imprime directamente la palabra ingresada
    return output


message = input(">")
print(emoji_converter(message))


