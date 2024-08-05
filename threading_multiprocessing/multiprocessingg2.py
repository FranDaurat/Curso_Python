#!/usr/bin/python3

import multiprocessing
import requests
import time

def petition(url):
    response = requests.get(url)
    print(f"\n[+] URL [{url}]: {len(response.content)} bytes")

domains = [
    "https://google.es",
    "https://xvideos.com",
    "https://wikipedia.org",
    "https://yahoo.com"
]

processes = []

start_time = time.time()

for domain in domains:
    process = multiprocessing.Process(target=petition, args=(domain,))
    process.start()
    processes.append(process) # Agrego cada hilo a una lista processes

for process in processes:
    process.join() # Espero a que todos terminen

end_time = time.time()

print(f"\n[+] Tiempo total: {round(end_time - start_time, 2)} segundos")