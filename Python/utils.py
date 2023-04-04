# Funcion rehusable en relación con Ejercicio2

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


def find_max(list):
    maxim = list[0]
    for x in list:
        if x > maxim:
            maxim = x
    return maxim
