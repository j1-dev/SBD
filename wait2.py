import time

def tarea(n):
    total = 0
    for i in range(n):
        total += i
    return total

inicio = time.time()
for _ in range(5):
    tarea(20000000)
print(time.time()-inicio)