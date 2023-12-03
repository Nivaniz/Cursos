# Chat Server
import socket

# Definir constantes a usar
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12346
ENCODER = "utf-8"
BYTESIZE = 1024

# Crear un socket de servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Aceptar cualquier conexión y comentar conexión
print("El servidor esta activo...\n")
client_socket, client_address = server_socket.accept()
client_socket.send("Estas conectado al servidor...\n".encode(ENCODER))

# Enviar y recibir mensajes
while True:
    # Recibir información del cliente
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    
    #Salir si el socket del cliente quiere salir, de otra forma mostrar el mensaje
    if message == "salir":
        client_socket.send("Salir".encode(ENCODER))
        print("\nTerminando la conexión... bye!")
        break
    else:
        print(f"\n{message}")
        message = input("Mensaje: ")
        client_socket.send(message.encode(ENCODER))

# Cerrar el socket
server_socket.close()