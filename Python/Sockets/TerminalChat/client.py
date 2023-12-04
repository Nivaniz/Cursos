# Cliente Chat Room
import socket, threading

# Definir constantes a usar
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 1234
ENCODER = "utf-8"
BYTESIZE = 1024

# Crear un socket de cliente y conectarlo al servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def send_message():
    '''Enviar mensaje al servidor para ser mostrado'''
    while True:
        message = input("")
        client_socket.send(message.encode(ENCODER))
        
        
def recieve_message():
    '''Recibir un mensaje del servidor'''
    while True:
        try:
            # Recibir el mensaje del servidor
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            
            # Checar por el nombre, de otra forma mostrar el mensaje
            if message == "NOMBRE":
                name = input("¿Cuál es tu nombre?: ")
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            # Un error ocurrio, cerramos la conexión
            print("Ha sucedido un error...")
            client_socket.close()
            break


# Crear hilos para continuamente enviar y recibir mensajes
recieve_thread = threading.Thread(target=recieve_message)
send_thread = threading.Thread(target=send_message)

# Comenzar el cliente
recieve_thread.start()
send_thread.start()