""" Desde la terminal abierta en la carpeta de los archivos
   PS C:\Users\93885\PycharmProjects\Hello World> python DocTest.py si no sale nada es que todo está bien
   PS C:\Users\93885\PycharmProjects\Hello World> python DocTest.py -v
   Trying:
       suma(5, 10)
   Expecting:
       15
   ok
   1 items had no tests:
       __main__
   1 items passed all tests:
      1 tests in __main__.suma
   1 tests in 2 items.
   1 passed and 0 failed.
   Test passed.
   """

# Como añadir pruebas al código para comprobar su funcionamiento


def suma(a, b):
    """
    La función suma(a,b) recibe dos parámetros a y b
    Devuelve la suma de ambos

    >>> suma(5, 10)
    15

    >>> suma(10, "Hola")
    Traceback (most recent call last):
     ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

