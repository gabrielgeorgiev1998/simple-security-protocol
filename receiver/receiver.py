import socket

receiver_host_address = '127.0.0.1'
receiver_port = 55555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver_socket:
    receiver_socket.bind((receiver_host_address, receiver_port))
 