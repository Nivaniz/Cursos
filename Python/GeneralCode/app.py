import Convertidores  # Lo hacemos objeto de otro documento
from Convertidores import kilos_a_libras  # importar directamente funciones

kilos_a_libras(100)  # Solo llamamos la funcion sin el modulo entero

print(Convertidores.kilos_a_libras(70))  # Usamos las funciones con el objeto

