#Client GUI Chat 
import tkinter as tk, socket, threading
from tkinter import DISABLED, VERTICAL, END, NORMAL

#Definir ventana
root = tk.Tk()
root.title("Circle Talk")
root.iconbitmap("message_icon.ico")
root.geometry("600x600")
root.resizable(0,0)

# Definir fuentes y colores
my_font = ('Poppins', 13)
bg_color = "#F3EEEE"  # Beige 
button_color = "#BBCAD6"  # Azul claro
text_color = "#000000"  # Negro

#Definir constantes
ENCODER = 'utf-8'
BYTESIZE = 1024
global client_socket

def connect():
    '''Conectar a un servidor en una dirección IP/puerto específica.'''
    global client_socket

    #Borrar anteriores chats o información
    my_listbox.delete(0, END)

    #Conseguir la información
    name = name_entry.get()
    ip = ip_entry.get()
    port = port_entry.get()

    #Solo intentar establecer una conexión si los tres campos están completos
    if name and ip and port:
        #Se cumplen las condiciones para la conexión, intente la conexión.
        my_listbox.insert(0, f"{name} está esperando para conectarse con {ip} al {port}...")

        #Crear un socket de cliente para conectarse al servidor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))

        #Verificar que la conexión es válida
        verify_connection(name)
    else:
        #Las condiciones para la conexión no se cumplieron
        my_listbox.insert(0, "Información insuficiente para conectar...")


def verify_connection(name):
    '''Verificar que la conexión del servidor sea válida y pase la información requerida'''
    global client_socket

    #El servidor enviará un indicador si se realiza una conexión válida
    flag = client_socket.recv(BYTESIZE).decode(ENCODER)

    if flag == 'NAME':
        #Se realizó la conexión, envíe el nombre del cliente y espere la verificación.
        client_socket.send(name.encode(ENCODER))
        message = client_socket.recv(BYTESIZE).decode(ENCODER)

        if message:
            #El servidor envió una verificación, ¡la conexión es válida!
            my_listbox.insert(0, message)

            #Cambiar botón/estados de entrada
            connect_button.config(state=DISABLED)
            disconnect_button.config(state=NORMAL)
            send_button.config(state=NORMAL)

            name_entry.config(state=DISABLED)
            ip_entry.config(state=DISABLED)
            port_entry.config(state=DISABLED)

            #Crear un hilo para recibir continuamente mensajes del servidor
            recieve_thread = threading.Thread(target=recieve_message)
            recieve_thread.start()
        else:
            #No se recibió ningún mensaje de verificación.
            my_listbox.insert(0, "Conexión no verificada")
            client_socket.close()
    else:
        #No se envió ningún indicador de nombre, se rechazó la conexión
        my_listbox.insert(0, "Conexión denegada")
        client_socket.close()


def disconnect():
    '''Desconectar del servidor'''
    global client_socket
    client_socket.close()

    #Cambiar botón/estados de entrada
    connect_button.config(state=NORMAL)
    disconnect_button.config(state=DISABLED)
    send_button.config(state=DISABLED)

    name_entry.config(state=NORMAL)
    ip_entry.config(state=NORMAL)
    port_entry.config(state=NORMAL)


def send_message():
    '''Enviar un mensaje al servidor para ser transmitido.'''
    global client_socket

    #SEnviar un mensaje al servidor
    message = input_entry.get()
    client_socket.send(message.encode(ENCODER))

    #Limpiar la entrada
    input_entry.delete(0, END)


def recieve_message():
    '''Recibir un mensaje entrante del servidor'''
    global client_socket

    while True:
        try:
            #Recibir mensaje
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            my_listbox.insert(0, message)
        except:
            #Un error ocurrió, desconectamos del servidor
            my_listbox.insert(0, "Cerrando la conexión ... Hasta pronto!")
            disconnect()
            break


# GUI Layout
info_frame = tk.Frame(root, bg=bg_color)
output_frame = tk.Frame(root, bg=bg_color)
input_frame = tk.Frame(root, bg=bg_color)

info_frame.pack()
output_frame.pack(pady=10)
input_frame.pack()

# Info Frame Layout
name_label = tk.Label(info_frame, text="Nombre:", font=my_font, fg=text_color, bg=bg_color)
name_entry = tk.Entry(info_frame, borderwidth=3, font=my_font)
ip_label = tk.Label(info_frame, text="IP:", font=my_font, fg=text_color, bg=bg_color)
ip_entry = tk.Entry(info_frame, borderwidth=3, font=my_font)
port_label = tk.Label(info_frame, text="Puerto:", font=my_font, fg=text_color, bg=bg_color)
port_entry = tk.Entry(info_frame, borderwidth=3, font=my_font, width=10)
connect_button = tk.Button(info_frame, text="Conectar", font=my_font, bg=button_color, borderwidth=5, width=10, command=connect)
disconnect_button = tk.Button(info_frame, text="Desconectar", font=my_font, bg=button_color, borderwidth=5, width=10, state=DISABLED, command=disconnect)

name_label.grid(row=0, column=0, padx=2, pady=10)
name_entry.grid(row=0, column=1, padx=2, pady=10)
port_label.grid(row=0, column=2, padx=2, pady=10)
port_entry.grid(row=0, column=3, padx=2, pady=10)
ip_label.grid(row=1, column=0, padx=2, pady=5)
ip_entry.grid(row=1, column=1, padx=2, pady=5)
connect_button.grid(row=1, column=2, padx=4, pady=5)
disconnect_button.grid(row=1, column=3, padx=4, pady=5)

# Output Frame Layout
my_scrollbar = tk.Scrollbar(output_frame, orient=VERTICAL)
my_listbox = tk.Listbox(output_frame, height=20, width=55, borderwidth=3, bg=bg_color, fg=text_color, font=my_font, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

# Input Frame Layout
input_entry = tk.Entry(input_frame, width=45, borderwidth=3, font=my_font)
send_button = tk.Button(input_frame, text="Enviar", borderwidth=5, width=10, font=my_font, bg=button_color, state=DISABLED, command=send_message)
input_entry.grid(row=0, column=0, padx=5, pady=5)
send_button.grid(row=0, column=1, padx=5, pady=5)

# Configurar colores
root.config(bg=bg_color)
info_frame.config(bg=bg_color)
output_frame.config(bg=bg_color)
input_frame.config(bg=bg_color)

# Iniciar ventana
root.mainloop()