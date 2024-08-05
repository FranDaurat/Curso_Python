#!/usr/bin/python3

import threading
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

threads = []

start_time = time.time()

for domain in domains:
    thread = threading.Thread(target=petition, args=(domain,))
    thread.start()
    threads.append(thread) # Agrego cada hilo a una lista threads

for thread in threads:
    thread.join() # Espero a que todos terminen

end_time = time.time()

print(f"\n[+] Tiempo total: {round(end_time - start_time, 2)} segundos")