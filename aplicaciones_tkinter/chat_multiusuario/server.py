#!/usr/bin/python3 

import socket 
import threading
import ssl

def client_thread(cs, clients, usernames):
    
    username = cs.recv(1024).decode()
    usernames[cs] = username
    
    print(f"\n[+] El usuario {username} se ha conectado")

    for client in clients:
        if client is not cs:
            client.send(f"[+] El usuario {username} ha entrado al chat\n\n".encode())
    
    while True:
        try:
            message = cs.recv(1024).decode()

            if not message:
                break

            if message == "!usuarios":
                cs.sendall(f"\n[+] Listado de usuarios disponibles: {', '.join(usernames.values())}\n\n".encode())
                continue

            for client in clients:
                if client is not cs:
                    client.send(f"{message}\n".encode())
        except:
            break
    cs.close()
    clients.remove(cs)
    del usernames[cs]

def server_program():

    host = 'localhost'
    port = 12345 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # --> Permite reutilizar la dirección del socket sin esperar a que el puerto se libere.
    server_socket.bind((host, port)) # --> Asocia el socket a la dirección y puerto especificados.
    server_socket = ssl.wrap_socket(server_socket, keyfile="server-key.key", certfile="server-cert.pem", server_side=True)
    server_socket.listen()

    print(f"\n[+] En escucha de conexiones entrantes...")

    clients = []
    usernames = {}

    while True:
        cs, addr = server_socket.accept()
        clients.append(cs)

        print(f"\n[+] Se ha conectado un nuevo cliente: {addr}")

        thread = threading.Thread(target=client_thread, args=(cs, clients, usernames))
        thread.daemon = True
        thread.start()
    
    server_socket.close()

if __name__ == '__main__':
    server_program()