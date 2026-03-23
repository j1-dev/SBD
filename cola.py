import threading
import time
import random
import queue

cola = queue.Queue(maxsize=50)

def productor():
    for i in range(10):
        item = i
        print(f"Produciendo {item}")
        cola.put(item)
        time.sleep(random.random())

def consumidor():
    while True:
        item = cola.get()
        print(f"Consumiendo {item}")
        time.sleep(random.random())
        cola.task_done()

threading.Thread(target=productor).start()
threading.Thread(
    target=consumidor,
    daemon=True
).start()