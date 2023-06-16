# Para una mejor explicacion de los errores
import unittest


def doblar(a): return a*2


class PruebasTestFixure(unittest.TestCase):

    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]

    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 11])

    def testDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)


if __name__ == "__main__":
    unittest.main()
'''
Traceback (most recent call last):
AssertionError: Lists differ: [2, 4, 6, 8, 10] != [2, 4, 6, 8, 11]

First differing element 4:
10
11

- [2, 4, 6, 8, 10]
?               ^

+ [2, 4, 6, 8, 11]
?               ^
'''
'''
Preparando el contexto
Realizando una prueba
.Preparando el contexto
Destruyendo el contexto
.
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''