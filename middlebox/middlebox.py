import socket
import threading

def middlebox(address, send_to_port, middlebox_port, type):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as middlebox_socket:
            middlebox_socket.bind((address, middlebox_port))
            print("Bound")

            middlebox_socket.listen()
            print("Listening")
            
            connected = False
            while not connected:
                try:
                    middlebox_socket.connect((address, send_to_port))
                    connected = True
                except Exception as e:
                    print(address)
                    print(e)
            
            print(type, " socket connected to ", address, ", port ", send_to_port)

            sender_connection, sender_address = middlebox_socket.accept()
            with sender_connection:
                print('Connected by ', sender_address)

                while True:
                    data = sender_connection.recv(4096)
                    if not data:
                        break
                    print(type, " data: ", data)
                    middlebox_socket.sendall(data)

#to differentiate between terminal windows
print("Middlebox")

address = '127.0.0.2'

receiver_port = 55555
sender_port = 55556

receiver_mid_port = 55557
sender_mid_port = 55558

sender_middlebox = threading.Thread(target=middlebox, args=(address, sender_port, sender_mid_port, 'Sender'))
sender_middlebox.start()

receiver_middlebox = threading.Thread(target=middlebox, args=(address, receiver_port, receiver_mid_port, 'Receiver'))
receiver_middlebox.start()
