# TCP client side

import socket

# Crear un socket de cliente IPV4 (AF_INET) y TCP (SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket a un servidor ubicado a un IP y Puerto dado
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

# Recibir un mensaje del servidor, especificando el max numero de bites a recibir
message = client_socket.recv(1024)
print(message.decode("utf-8"))


# Cerrar el socket del cliente
client_socket.close()