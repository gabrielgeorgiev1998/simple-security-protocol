import socket

middlebox_host_address = '127.0.0.1'
middlebox_port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
    sender_socket.connect((middlebox_host_address, middlebox_port))
    print("Connected to ", middlebox_host_address, ", port ", middlebox_port)

    sender_socket.sendall(b'helloworld')