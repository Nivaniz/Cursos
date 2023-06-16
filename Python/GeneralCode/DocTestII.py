def palindromo(palabra):
    """
    La función recibe una palabra.
    Si la palabra es un palíndromo devuelve True, si no False

    Un palindromo es una palabra que se lee [...]

    >> palindromo("radar")
    True

    >> palindromo("somos")
    True

    >> palindromo("holah")
    False

    >> palindromo("Ana")
    True

    >> palindromo("Atar a la rata")
    True
    """

    if palabra.lower().replace(" ", "") == palabra[::-1].lower().replace(" ", ""):
        return True
    else:
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Nos sale la ventana para ver cuantos test pasaron
