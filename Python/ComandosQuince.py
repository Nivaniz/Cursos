# Herencia multiple
# Hace referencia a que una subclase herede de muchas subclases
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")


class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")

class C(A, B):
    pass  # Que herede de clase a y b
    def c(self):
        print("Este método es de C")


c = C()

c.a()  # Este método lo heredo de A
c.b()  # Este método lo heredo de B
c.c()  # Este método lo heredo de C