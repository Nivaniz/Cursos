# UDP Cliente
import socket

# Crear un socket del cliente usando IPV4 (AF_INET) y UDP (SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar información mediante una via sin conexión del protocolo
client_socket.sendto("Has entrado al Servidor".encode("utf-8"), (socket.gethostbyname(socket.gethostname()), 12345))