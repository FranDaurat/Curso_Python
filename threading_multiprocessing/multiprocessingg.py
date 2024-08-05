#!/usr/bin/python3 

import multiprocessing
import time

def tarea(num_tarea):
    print(f"\n[+] Proceso {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Proceso {num_tarea} finaliando")

proceso1 = multiprocessing.Process(target=tarea, args=(1,))
proceso2 = multiprocessing.Process(target=tarea, args=(2,))

proceso1.start()
proceso2.start()

proceso1.join()
proceso2.join()

