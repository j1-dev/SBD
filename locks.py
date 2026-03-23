# Ejemplo previo
import threading
from random import random
import time

lock = threading.Lock()

def procesar(n):
    global total
    with lock:
        temp = total
        time.sleep(random()*0.001)
        total = temp + n * n

total = 0
hilos = []

for i in range(100):
    t = threading.Thread(target=procesar, args=(i,))
    hilos.append(t)
    t.start()

for t in hilos:
    t.join()
print(total)