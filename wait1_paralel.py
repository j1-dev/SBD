import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import freeze_support

def tarea(a):
    time.sleep(1)

if __name__ == '__main__':
    freeze_support()
    inicio = time.time()

    datos = [1,2,3,4,5]
    with ProcessPoolExecutor() as executor:
        resultados = list(executor.map(tarea,datos))

    print(time.time()-inicio)