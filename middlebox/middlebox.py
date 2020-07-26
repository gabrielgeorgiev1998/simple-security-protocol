import socket

receiver_host_address = '127.0.0.1'
receiver_port = 55555

middlebox_host_address = '127.0.0.1'
middlebox_port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as middlebox_socket:
    middlebox_socket.bind((middlebox_host_address, middlebox_port))
    print("Bound")

    middlebox_socket.listen()
    print("Listening")

    sender_connection, sender_address = middlebox_socket.accept()
    with sender_connection:
        print('Connected by ', sender_connection)

        while True:
            data = sender_connection.recv(1024)
            if not data:
                break
            print(data)
