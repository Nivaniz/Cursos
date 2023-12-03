# Chat CLIENT
import socket

# Definir constantes a usar
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12346
ENCODER = "utf-8"
BYTESIZE = 1024

# Crear un socket de cliente y conectarlo al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# Recibir y enviar mensajes
while True:
    # Recibir información del servidor
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    
    # Salir si el servidor conectado quiere salir si no seguir enviando mensajes
    if message == "salir":
        client_socket.send("Salir".encode(ENCODER))
        print("\nTerminando la conexión... bye!")
        break
    else:
        print(f"\n{message}")
        message = input("Mensaje: ")
        client_socket.send(message.encode(ENCODER))

# Cerrar el socket
client_socket.close()