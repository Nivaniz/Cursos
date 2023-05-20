# Comentamos con gato o dobles comillas

# Imprimimos con:
print("Hello")
print('o----')
print('||||' * 5)

# Variables
price = 10  # Integrer
rating = 4.9  # Float
name_new = 'Mosh'  # String
is_published = True  # Boolean
print(price)  # No ocupamos las comillas por que lo imprimirá como string

# Recibir un input
name = input('What is your name? ')  # Nos da un resultado y lo guardamos en una variable
color = input('¿Whats your favorite color? ')
print(name + ' likes ' + color)  # Concatenación

# Type conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2023 - int(birth_year)  # 2023 - '2003'
print(type(age))
print(age)

# Strings
Course = "Python's course for beginners"
Course_Two = 'Python for "Beginners"'
Course_Three = '''
Hi, John,

Here is the mail you wanted
Congratulations!
'''
print(Course_Three)
print(Course[0])  # P
print(Course[-1])  # s
print(Course[0:3])  # Pyt
print(Course[1:])  # ython's course for beginners

#  Ejemplo
name_J = 'Jennifer'
print(name[1:-1])  # ennife

#  Strings Formateados
first = 'John'
last = 'Mary'
msg = f'{first} [{last}] is a coder'
print(msg)  # Es igual que first + ' [ ' + last + '] is a coder


#  Métodos de Strings
course = 'Python for Beginners'
print(len(course))  # Imprimir el tamaño
print(course.upper())  # Imprimir en mayusculas
#  .find ('P') encontrar el index string
#  .replace ('for', 'my')
# in regresa booleano
print('Python' in course)  # True
print('python' in course)  # False

