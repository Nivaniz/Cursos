# UDP Server
import socket

# Crear un socket del servidor usando IPV4 (AF_INET) y UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Establecer nuestro socket a una tupla (Direccion IP, Direccion del Puerto)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

# No vamos a escuchar o aceptar coneciones ya que UDP es un protocol sin conexiones
message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(address)