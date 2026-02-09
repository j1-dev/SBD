import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support

def tarea(tupla):
    inicio = tupla[0]
    fin = tupla[1]
    total = 0
    for i in range(inicio, fin):
        total += i
    return total

if __name__ == '__main__':
    freeze_support()
    inicio = time.time()

    rangos = [(0,50000000), (50000000, 10000000)]
    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(tarea,rangos))

    print(time.time()-inicio)
    print(sum(resultados))