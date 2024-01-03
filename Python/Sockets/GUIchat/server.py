# Servidor de Sala de Chat
import socket
import threading

# Define las constantes a utilizar
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024
# 192.168.77.1

# Crea un socket de servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Crea dos listas vacías para almacenar los sockets de clientes conectados y sus nombres
client_socket_list = []
client_name_list = []

def broadcast_message(message):
    '''Envía un mensaje a TODOS los clientes conectados al servidor'''
    for client_socket in client_socket_list:
        client_socket.send(message)

def recieve_message(client_socket):
    '''Recibe un mensaje entrante de un cliente específico y reenvía el mensaje para ser transmitido'''
    while True:
        try:
            # Obtiene el nombre del cliente dado
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]
            
            # Recibe el mensaje del cliente
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            message = f"{name}: {message}".encode(ENCODER)
            broadcast_message(message)
        except:
            # Encuentra el índice del socket del cliente en nuestra lista
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            # Elimina el socket del cliente y el nombre de las listas
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            # Cierra el socket del cliente
            client_socket.close()

            # Transmite que el cliente ha abandonado la sala de chat.
            broadcast_message(f"{name} ha abandonado la sala de chat.".encode(ENCODER))
            break

def connect_client():
    '''Conecta a un cliente entrante al servidor'''
    while True:
        # Acepta cualquier conexión entrante de cliente
        client_socket, client_address = server_socket.accept()
        print(f"Conectado con {client_address}...")

        # Envía una bandera NAME para solicitar al cliente su nombre
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        # Agrega el nuevo socket del cliente y el nombre del cliente a las listas apropiadas
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        # Actualiza el servidor, el cliente individual y TODOS los clientes
        print(f"Nombre del nuevo cliente: {client_name}\n")  # servidor
        client_socket.send(f"{client_name}, te has conectado al servidor.".encode(ENCODER))  # Cliente individual
        broadcast_message(f"{client_name} se ha unido a la sala de chat.".encode(ENCODER))

        # Ahora que un nuevo cliente se ha conectado, inicia un hilo
        recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
        recieve_thread.start()

# Inicia el servidor
print("El servidor está escuchando las conexiones entrantes...\n")
connect_client()
