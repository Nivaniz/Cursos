import threading

# Hilos nos ayuda a acelerar los programas ejecutando multiples tareas al mismo tiempo
# Cada tarea corre en su propio hilo
# Cada hilo puede correr simultaneamente y compartir data con otros

# Cada hilo cuando comienza debe hacer algo, que podemos definir con una función
# Nuestros hilos se relacionaran con las funciones
# Cuando comenzamos estos hilos, estas funciones se ejecutaran

def funcion1():
    for i in range(10):
        print("Uno ")

def funcion2():
    for i in range(10):
        print("Dos ")

def funcion3():
    for i in range(10):
        print("Tres ")
        
# Si llamamos estas funciones, vemos que la primera funcion debe completarse antes de la siguiente linealmente

# Podemos ejecutar las funciones concurrentemente con hilos
t1 = threading.Thread(target=funcion1)
t2 = threading.Thread(target=funcion2)
t3 = threading.Thread(target=funcion3)

# Comenzar el hilo
t1.start()
t2.start()
t3.start()