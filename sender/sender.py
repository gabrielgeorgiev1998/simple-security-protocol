import socket

if __name__=='__main__':
    df_mod = 23
    df_base = 5

    df_secret = 4 

    address = '127.0.0.1'

    sender_port = 55556

    middlebox_port = 55558

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender_socket:
        sender_socket.bind((address, sender_port))
        print("Bound")

        connected = False
        while not connected:
            try:
                sender_socket.connect((address, middlebox_port))
                connected = True
            except:
                pass
        print("Connected to ", address, ", port ", middlebox_port)
        
        num = input()
        sender_socket.send(bytes(num, 'utf-8'))