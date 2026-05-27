import socket
import threading
import sys

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER = socket.gethostbyname(socket.gethostname())                   # you can use the host ip
PORT = 9687
USERNAME = input("Enter the Username: ")

try:
    client_sock.connect((SERVER, PORT))
    print(f"Successfully connected with the server {SERVER}:{PORT}\n\n")
except:
    print("Unable to connect to the server. Try Again...")
    exit()

def recieve():
    while True:
        message = client_sock.recv(1024).decode()
        temp = message.split(":")

        if temp[0] == USERNAME:
            continue

        if message:
            print(f"\033[93m{message}\033[0m")
        else:
            print("An unknown error occurred")
            client_sock.close()
            break

def send():
    while True:
        message = input("")
        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()
        print(f"\033[94m{message}\033[0m")
        if message:
            try:
                client_sock.sendall(f"{USERNAME}: {message}".encode('utf-8'))
            except:
                print("An error occurred")
                client_sock.close()
                break

recieve_thread = threading.Thread(target=recieve)
send_thread = threading.Thread(target=send)
recieve_thread.start()
send_thread.start()