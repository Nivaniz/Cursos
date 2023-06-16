# Expresiones regulares
import re

# Permite buscar un patron en una cadena
texto = "En esta cadena se encuentra una palabra mágica"
print(re.search('mágica', texto))  # <re.Match object; span=(40, 46), match='mágica'>
# Si no existe no se nos devuelve nada

palabra = "mágica"
encontrada = re.search(palabra, texto)

if encontrada is not None:
    print("Se ha encontrado la palabra")
else:
    print("No se ha encontrado la palabra")

print(encontrada.start())  # La posicion en donde se encuentra la palabra 40
print(encontrada.end())  # Donde termina 46
print(encontrada.span())  # Tupla (40,46)

# Permite buscar un patron al principio de otra cadena
texto1 = "Hola mundo"
print(re.match("Hola", texto1))  # <re.Match object; span=(0, 4), match='Hola'>

# Dividir una cadena a partir de un patron
texto2 = "Vamos a dividir esta cadena"
print(re.split(' ', texto2))  # ['Vamos', 'a', 'dividir', 'esta', 'cadena']

# Substituir una cadena
texto3 = "Vamos a dividir esta cadena"
print(re.sub('esta', 'este', texto2))  # Vamos a dividir este cadena

# Busca todas las coincidencias en una cadena
texto4 = "hola adios hola hola"
print(re.findall('hola', texto4))  # ['hola', 'hola', 'hola']

print(len(re.findall('hola', texto4)))  # numero de veces que se repite 3

texto5 = "hola adios hello hola"
print(re.findall("(hola|hello)", texto5))  # ['hola', 'hello', 'hola']

# Patrones con sintaxis repetidas
texto6 = "hla hola hoola holaaaaaa hoooola"

print("____________________________________")
def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))


patrones = ["hla" , "holaaaaaa", "hoooola"]
buscar(patrones, texto6) # ['hla'] ['holaaaaaa'] ['hoooola']

# Ninguna o más repeticiones de la letra a su izquierda
pattron = ['ho', 'ho*', 'ho*la', 'hu*la']

'''el * indica que la letra o a la izquierda de la letra h 
puede aparecer cero o más veces. Por lo tanto, la función 
re.findall() busca todas las apariciones de h seguidas de 
cero o más ocurrencias de o en el texto texto6 o sea que la o
se repita 0 o más veces'''

buscar(pattron, texto6)
''''
['ho', 'ho', 'ho', 'ho']
['h', 'ho', 'hoo', 'ho', 'hoooo']
['hla', 'hola', 'hoola', 'hola', 'hoooola']
['hla']
'''

print("_____________________________")
# Se repite la o 1 o más veces +
# Se repite 0 o más veces *
# Se repite la letras antes una o ninguna ?
pattron2 = ['ho*', 'ho+', 'ho?', 'ho?la']
buscar(pattron2, texto6)

'''
['h', 'ho', 'hoo', 'ho', 'hoooo']
['ho', 'hoo', 'ho', 'hoooo']
['h', 'ho', 'ho', 'ho', 'ho']
['hla', 'hola', 'hola']
'''

# Indicar el número de repeticiones
pattron3 = ['ho{0}la']  # Donde la o se repite 0 veces
buscar(pattron3, texto6)  # ['hla']

pattron4 = ['ho{0,1}la']  # Cuando la o se repita de 0 a una vez
buscar(pattron4, texto6)  # ['hla', 'hola', 'hola']

print("_____________________________")

texto7 = "hala hela hila hola hula"
pattron5 = ['h[ou]la', 'h[oui]la', 'h[^o]la']
buscar(pattron5, texto7)

'''
['hola', 'hula'] palabras que tengan la o o la u
['hila', 'hola', 'hula'] palabras que tengan la o,u,i
['hala', 'hela', 'hila', 'hula'] para indicar una busqueda contraria
'''

print("_____________________________")

texto8 = "Este curso de Python 3 se hizo en el 2016"
pattron6 = [r'\d', r'\d+', r'\s', r'\S', r'\S+']
buscar(pattron6, texto8)

'''
['3', '2', '0', '1', '6'] solo numeros
['3', '2016'] numeros completos
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] espacios
['E', 's', 't', 'e', 'c', 'u', 'r', 's...] todas las letras menos los espacios
['Este', 'curso', 'de', 'Python', '3', 'se', 'hizo', 'en', 'el', '2016'] las palabras
'''