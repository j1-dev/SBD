# Ejemplo previo
import threading
from random import random
import time

lock_A = threading.Lock()
lock_B = threading.Lock()

def procesar_1(n):
    global total
    with lock_A:
        temp = total
        time.sleep(random()*0.001)
        total = temp + n * n
        print("Tarea 1 intenta adquirir lock B")
        if lock_B.acquire(timeout=1):
            with lock_B:
                print("Tarea 1 adquiere lock B")

def procesar_2(n):
    global total
    with lock_B:
        temp = total
        time.sleep(random()*0.001)
        total = temp + n * n
        print("Tarea 2 intenta adquirir lock A")
        if lock_A.acquire(timeout=1):
            with lock_A:
                print("Tarea 2 adquiere lock A")

total = 0
hilos = []

for i in range(10):
    t1 = threading.Thread(target=procesar_1, args=(i,))
    t2 = threading.Thread(target=procesar_2, args=(i,))
    hilos.append(t1)
    hilos.append(t2)
    t1.start()
    t2.start()

for t in hilos:
    t.join()

print(total)