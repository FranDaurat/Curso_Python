#!/usr/bin/python3 

import socket
import threading
import ssl
from tkinter import * 
from tkinter.scrolledtext import ScrolledText


def send_message(cs, username, text_widget, entry_widget):
    
    message = entry_widget.get()
    cs.sendall(f"{username}: {message}".encode())

    entry_widget.delete(0, END)
    text_widget.configure(state='normal')
    text_widget.insert(END, f"{username}: {message}\n")
    text_widget.configure(state='disabled')


def receive_message(cs, text_widget):
    while True:
        try:
            message = cs.recv(1024).decode()

            if not message:
                break

            text_widget.configure(state='normal')
            text_widget.insert(END, message)
            text_widget.configure(state='disabled')
        except:
            break

def list_users(cs):
    cs.sendall("!usuarios".encode())

def exit(cs, username, window):
    
    cs.sendall(f"\n[!] El usuario {username} ha abandonado el chat\n".encode())
    cs.close()

    window.quit()
    window.destroy()

def client_program():
    
    host = 'localhost'
    port = 12345

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs = ssl.wrap_socket(cs)
    cs.connect((host, port))

    username = input(f"\n[+] Introduce tu usuario: ")
    cs.sendall(username.encode())

    window = Tk()
    window.title("Chat")

    text_widget = ScrolledText(window, state='disabled')
    text_widget.pack(padx=5, pady=5)

    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=2, fill=BOTH, expand=1)

    entry_widget = Entry(frame_widget, font=("Arial", 14))
    entry_widget.bind("<Return>", lambda _: send_message(cs, username, text_widget, entry_widget))
    entry_widget.pack(side=LEFT, fill=X, expand=1)
 
    button_widget = Button(frame_widget, text="Enviar", command=lambda: send_message(cs, username, text_widget, entry_widget))
    button_widget.pack(side=RIGHT, padx=5)

    users_widget = Button(window, text="Listar usuarios", command=lambda: list_users(cs))
    users_widget.pack(padx=5, pady=5)

    exit_widget = Button(window, text="Salir", command=lambda: exit(cs, username, window))
    exit_widget.pack(padx=5, pady=5)

    thread = threading.Thread(target=receive_message, args=(cs, text_widget))
    thread.daemon = True
    thread.start()

    window.mainloop()
    cs.close()


if __name__ == '__main__':
    client_program()