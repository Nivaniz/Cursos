# TCP Server Side
import socket

# Crear un socket del servidor usando IPV4 (AF_INET) y TCP (SOCK_STREAM)
# AF_INET : familia de direcciones IPv4
# SOCK_STREAM:  se refiere a un socket de flujo orientado a la conexión utilizado para la comunicación bidireccional 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conseguir la Dirección IP dinamicamente
# print(socket.gethostname())
# print(socket.gethostbyname(socket.gethostname()))

# Establecer nuestro socket a una tupla (Direccion IP, Direccion del Puerto)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# Poner el socket en modo escucha para que escuche cualquier posible conexión
server_socket.listen()

# Escuhar eternamente para que acepte cualquier conexión
while True:
    # Aceptar cada conexión y cuadarla en dos pedazos dde información
    client_socket, client_address = server_socket.accept()
    
    # Mensaje que alguien se conectó
    print(f"Conectado a {client_address}\n")
    
    # Enviar un mensaje al cliente que se acaba de conectar
    client_socket.send("Estas conectado!".encode("utf-8"))
    
    # Cerrar la conexión
    server_socket.close()
    break