""" Para documentar desde la terminal abrimos cmd desde la careta cn el archivo
a documentar y escribimos pydoc -w mi_modulo, y se nos va a crear un html para
editar la documentación, si fuese un paquete es pydoc -w mi_paquete .\ """

# Documentar funciones

def hola(args):
    """ Este es el docstring de la función"""
    print("Hola", args, "!")


hola("Nirvana")
# Para recuperar la documentacion de la función:
help(hola)  # hola(args) Este es el docstring de la función


# Documentar clases
class Clase:
    """ Este es el docstring de la clase"""

    def __init__(self):
        """ Este es el docstring del inicializador de la clase"""
        pass

    def metodo(self):
        """ Este es el docstring del método clase"""
        pass


o = Clase()
help(o)

'''
class Clase(builtins.object)
 |  Este es el docstring de la clase
 |  
 |  Methods defined here:
 |  
 |  __init__(self)
 |      Este es el docstring del inicializador de la clase
 |  
 |  metodo(self)
 |      Este es el docstring del método clase
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
'''

# Para documentar modulos

# import mi_modulo
""" Este es el docstring del módulo"""
def despedir():
    """Este es el docstring dde la función despedir"""
    print("Adiós! Me estoy despidiendo desde la función despedit() del módulo")

# mi_modulo.despedir()
# help(mi_modulo)


# Para documenar un paquete
# En la primera línea del __init__
# import mi_paquete

'''
Name 
    mi_paquete = Este es el docstring de mi_paquete
    
Package contents
    adios(package)
    hola(pacacke)
    
File
    ................
'''