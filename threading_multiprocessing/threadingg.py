#!/usr/bin/python3

import threading
import time

def tarea(num_tarea):
    print(f"\n[+] Hilo {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Hilo {num_tarea} iniciando")

thread1 =  threading.Thread(target=tarea, args=(1,))
thread2 =  threading.Thread(target=tarea, args=(2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"\n[+] Los hilos finalizaron")