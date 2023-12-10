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

#Define socket constants
ENCODER = 'utf-8'
BYTESIZE = 1024
global client_socket

#Define Functions
def connect():
    '''Connect to a server at a given ip/port address'''
    global client_socket

    #Clear any previous chats
    my_listbox.delete(0, END)

    #Get the required connection information
    name = name_entry.get()
    ip = ip_entry.get()
    port = port_entry.get()

    #Only try to make a connection if all three fields are filled in
    if name and ip and port:
        #Conditions for connection are met, try for connection
        my_listbox.insert(0, f"{name} is waiting to connect to {ip} at {port}...")

        #Create a client socket to connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))

        #Verify that the connection is valid
        verify_connection(name)
    else:
        #Conditions for connection were not met
        my_listbox.insert(0, "Insufficient information for connection...")


def verify_connection(name):
    '''Verify that the server connection is valid and pass required information'''
    global client_socket

    #The server will send a NAME flag if a valid connection is made
    flag = client_socket.recv(BYTESIZE).decode(ENCODER)

    if flag == 'NAME':
        #The connection was made, send client name and await verification
        client_socket.send(name.encode(ENCODER))
        message = client_socket.recv(BYTESIZE).decode(ENCODER)

        if message:
            #Server sent a verification, connection is valid!
            my_listbox.insert(0, message)

            #Change button/entry states
            connect_button.config(state=DISABLED)
            disconnect_button.config(state=NORMAL)
            send_button.config(state=NORMAL)

            name_entry.config(state=DISABLED)
            ip_entry.config(state=DISABLED)
            port_entry.config(state=DISABLED)

            #Create a thread to contiuously recieve messages from the server
            recieve_thread = threading.Thread(target=recieve_message)
            recieve_thread.start()
        else:
            #No verification message was recieved
            my_listbox.insert(0, "Connection not verified.  Goodbye...")
            client_socket.close()
    else:
        #No name flag was sent, connection was refused
        my_listbox.insert(0, "Connection refused.  Goodbye...")
        client_socket.close()


def disconnect():
    '''Disconnect from the server'''
    global client_socket

    #Close the socket
    client_socket.close()

    #Change button/entry states
    connect_button.config(state=NORMAL)
    disconnect_button.config(state=DISABLED)
    send_button.config(state=DISABLED)

    name_entry.config(state=NORMAL)
    ip_entry.config(state=NORMAL)
    port_entry.config(state=NORMAL)


def send_message():
    '''Send a message to the server to be broadcast'''
    global client_socket

    #Send the message to the server
    message = input_entry.get()
    client_socket.send(message.encode(ENCODER))

    #Clear the input entry
    input_entry.delete(0, END)


def recieve_message():
    '''Recieve an incoming message from the server'''
    global client_socket

    while True:
        try:
            #Recivee an incoming message from the server
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            my_listbox.insert(0, message)
        except:
            #An error occured, disconnect from the server
            my_listbox.insert(0, "Closing the connection.  Goodbye...")
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

# Configure colors
root.config(bg=bg_color)
info_frame.config(bg=bg_color)
output_frame.config(bg=bg_color)
input_frame.config(bg=bg_color)

# Run the root window's mainloop()
root.mainloop()