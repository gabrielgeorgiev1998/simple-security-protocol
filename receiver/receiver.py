import socket

#to differentiate between terminal windows
print("Receiver")

df_mod = 23
df_secret = 3



address = '127.0.0.3'
receiver_port = 55555

middlebox_port = 55557

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver_socket:
    receiver_socket.bind((address, receiver_port))
    print("Bound")

    receiver_socket.listen()
    print("Listening") 
    
    connected = False
    while not connected:
        try:
            receiver_socket.connect((address, middlebox_port))
            connected = True
        except:
            pass
    

    middlebox_connection, middlebox_address = receiver_socket.accept()
    with middlebox_connection:
        print('Connected by ', middlebox_connection)

        while True:
            data = middlebox_connection.recv(1024)
            if not data:
                break
            print(data)
