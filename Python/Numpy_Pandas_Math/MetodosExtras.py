import numpy as np

# Generamos un array de 2*3 con numeros aleatorios
arr = np.arange(1, 7).reshape(2, 3)
print(arr)

'''
[[1 2 3]
 [4 5 6]]
'''

# Suma todos los elementos de un array
print(arr.sum())  # 21
# Media
print(arr.mean())  # 3.5
# Desviación
print(arr.std())  # 1.707825127659933
# Varianza
print(arr.var())  # 2.9166666666666665

print('________________________')
arrr = np.random.randint(-10, 10, [3, 3])
# Ordenar horizontalmente
arrr.sort()
print(arrr)  # Ordena de - a + [ -7  -2   9]]
# Ordenar verticalmente
arrr.sort(0)
print(arrr)

'''
[[-9 -4 -4]
 [-7 -4  1]
 [-5  2  8]]
'''

# Almacenar Arrays y tener persistencia
# GUARDADO BINARIO (no se puede modificar pero permite guardar varios)
# creamos un array aleatorio
print("_____________")
arr_1 = np.random.randint(0, 4, [3, 3])
np.save('arr_1.npy', arr_1)
# Si se borra como del(arr_1) ya no aparecerá cargado
# Se puede volver a cargar con arr_1 = np.load('arr_1.npy')
'''
[[1 2 2]
 [1 3 1]
 [3 3 0]]
'''

'''
GUARDADO DE TEXTO (se puede modificar pero solo te deja guardar uno)
utilizaremos savez para guardar de forma comprimida con la extensión .npz debemos especificar una clave para cada array que queramos guardar
np.savez('arrays.npz', arr_1=arr_1, arr_2=arr_2)
Podemos acceder a ellas mediante su clave: arrays['arr_1']

Para guardar en texto es igual pero usamos savetxt() y loadtxt()
np.savetxt('arr_1.txt', arr_3)
'''

