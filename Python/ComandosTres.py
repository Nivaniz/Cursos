# While loops
i = 1
while i <= 5:  # Mientras sea verdadero el código de abajo se va repetir consecutivamente
    print(i)
    i = i + 1  # Así se hace falso y no se repite
print("Done")

numero = 9
atinos_contados = 0
atinos_max = 3

while atinos_contados < atinos_max:
    atino = int(input('Guess: '))
    atinos_contados += 1
    if atino == numero:  # SI ES TRUE
        print("Ganaste!")
        break  # Rompe el ciclo
else:  # Si el código se completa sin el if suelta
    print("Sorry you fail")