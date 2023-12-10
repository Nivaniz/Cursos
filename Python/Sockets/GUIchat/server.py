# Server Chat Room
import socket, threading

# Definir constantes a usar
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 1234
ENCODER = "utf-8"
BYTESIZE = 1024

# Colores ANSI para la consola
COLORS = ["\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]


# Crear un socket de servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Crear dos listas para guardar clientes y sus nombres
client_socket_list = []
client_name_list = []

def broadcast_message(message, sender_socket):
    '''Enviar un mensaje a todos los clientes conectados excepto al remitente'''
    for client_socket in client_socket_list:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                # Manejar errores al enviar mensajes a clientes específicos (si es necesario)
                pass


def recieve_message(client_socket):
    '''Recibir un mensaje de un cliente especifico y enviarlo a la principal'''
    while True:
        try:
            # Conseguir el nombre y color del cliente
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]
            color = COLORS[index % len(COLORS)]  # Asignar un color único a cada cliente
            
            # Recibir mensaje del cliente
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            
            # Formatear el mensaje con el nombre y color del cliente
            formatted_message = f"{color}\t{name}: {message}\033[0m".encode(ENCODER)
            
            # Enviar el mensaje a todos los demás clientes
            broadcast_message(formatted_message, client_socket)
            
            # Además, enviar el propio mensaje con formato al cliente que lo envió
            client_socket.send(formatted_message)
        except ConnectionResetError:
            # Manejar la desconexión del cliente
            handle_client_disconnection(client_socket)
            break
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")


def handle_client_disconnection(disconnected_socket):
    '''Manejar la desconexión de un cliente'''
    index = client_socket_list.index(disconnected_socket)
    name = client_name_list[index]

    # Eliminar el cliente y el nombre de nuestras listas
    client_socket_list.remove(disconnected_socket)
    client_name_list.remove(name)

    # Cerrar el socket del cliente
    disconnected_socket.close()
    
    # Anunciar que el cliente ha salido del chat
    broadcast_message(f"\033[5;91m\t{name} ha salido del chat!\033[0m".encode(ENCODER), disconnected_socket)

        
def connect_client():
    '''Conectar un cliente al servidor'''
    while True:
        # Aceptar cualquier conexión del cliente
       client_socket, client_address = server_socket.accept()
       print(f"Conectado con {client_address}...")
       
       # Enviar un mensaje para que el cliente ponga su nombre
       client_socket.send("NOMBRE".encode(ENCODER))
       client_name = client_socket.recv(BYTESIZE).decode(ENCODER)
       
       # Agregar un nuevo socket de cliente y el nombre del cliente a sus listas
       client_socket_list.append(client_socket)
       client_name_list.append(client_name)
       
       # Actualizar el servidor, el cliente individual y todos los clientes
       print(f"El nuevo usuario es {client_name}\n") # Servidor
       client_socket.send(f"{client_name}, te has conectado al servidor!".encode(ENCODER)) # Individual
       
       # Agregar sender_socket aquí
       sender_socket = None  
       broadcast_message(f"{client_name} se ha unido al chat!".encode(ENCODER), sender_socket)
       
       # Ahora que un nuevo cliente se ha conectado, comenzamos un hilo
       recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
       recieve_thread.start()


# Comenzar el servidor
print("El servidor está escuchando por conexiones...\n")
connect_client()