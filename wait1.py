import time

def tarea():
    time.sleep(1)

inicio = time.time()
for _ in range(5):
    tarea()
print(time.time()-inicio)