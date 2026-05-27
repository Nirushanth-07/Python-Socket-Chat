import socket
import select

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9687
clients = []

server_sock.bind((SERVER, PORT))
print(f"connection has been established {SERVER}:{PORT}\n")
server_sock.listen(5)

while True:
    recieved_clients, _, exception_clients = select.select([server_sock]+clients, [], clients)

    for Socket in recieved_clients:
        if Socket == server_sock:
            client_sock, client_address = server_sock.accept()
            print(f"New connection from {client_address}")
            clients.append(client_sock)
        else:
            try:
                message = Socket.recv(1024)

                if message:
                    for client in clients:
                        if client != server_sock:
                            client.sendall(message)         
                else:
                    Socket.close()
                    clients.remove(Socket)
            except:
                Socket.close()
                clients.remove(Socket)
                continue
    