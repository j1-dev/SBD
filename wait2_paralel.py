import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support

def tarea(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == '__main__':
    inicio = time.time()

    datos = [200000000,200000000,200000000,200000000,200000000,200000000,200000000,200000000]
    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(tarea,datos))

    print(time.time()-inicio)
    print(resultados)