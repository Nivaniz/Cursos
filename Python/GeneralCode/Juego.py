comando = ""
started = False

# si ya dimos start que diga que ya está prendido, # si dimos que stop que diga que ya paró
while True:
    comando = input(">").upper()
    if comando == 'START':
        if started:  # TRUE QUE NO LO ES SALTA
            print("Car is already started")
        else:
            started = True  # SE CAMBIA A TRUE Y YA ESTÁ INICIADO
            print("The car is running")
    elif comando == 'STOP':
        if not started:  # SI STARTED ESTA EN FALSE
            print("Car is already stropped")
        else:
            started = False  # SE QUITA EL INICIADO  VUELVE A FALSO
            print("Car Stopped")
    elif comando == 'HELP':
        print("Start - to start the car")
        print("Stop - to stop the car")
        print("Quit - to exit")
    elif comando == "QUIT":
        break
    else:
        print("I don´t understand that... try again")