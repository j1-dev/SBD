import random
import time
import math
import multiprocessing


# Función primos 
def is_prime(n: int):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


# Productor 
def producer(queue, total_numbers, num_consumers):
    for _ in range(total_numbers):
        number = random.randint(10**11, 10**12 - 1)
        queue.put(number)

    # Señal de finalización
    for _ in range(num_consumers):
        queue.put(None)


# Consumidor 
def consumer(input_queue, output_queue):
    while True:
        number = input_queue.get()
        if number is None:
            break
        if is_prime(number):
            output_queue.put(number)


def main():
    total_numbers = 200
    num_consumers = multiprocessing.cpu_count()
    print("Num consumers: ", num_consumers)

    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    start = time.perf_counter()

    # Crear procesos consumidores
    consumers = []
    for _ in range(num_consumers):
        p = multiprocessing.Process(
            target=consumer,
            args=(input_queue, output_queue)
        )
        p.start()
        consumers.append(p)

    # Crear productor
    producer_process = multiprocessing.Process(
        target=producer,
        args=(input_queue, total_numbers, num_consumers)
    )
    producer_process.start()

    # Esperar a que termine productor
    producer_process.join()

    # Esperar consumidores
    for p in consumers:
        p.join()

    end = time.perf_counter()

    # Recoger resultados
    primes = []
    while not output_queue.empty():
        primes.append(output_queue.get())

    # Informe
    print(f"Total números generados: {total_numbers}")
    print(f"Números primos encontrados: {len(primes)}")
    print("\nLista de primos:")
    for p in primes:
        print(p)

    print(f"\nTiempo total de ejecución: {end - start:.4f} segundos")


if __name__ == "__main__":
    main()


# Ejemplo de output real
# 
# Num consumers:  16
# Total números generados: 200
# Números primos encontrados: 13
# 
# Lista de primos:
# 470847492937
# 292072570957
# 703332440029
# 442232008279
# 311172970037
# 421567152581
# 447552381989
# 439624984207
# 474528135283
# 542113904771
# 895057154179
# 838327880821
# 865326492119
# 
# Tiempo total de ejecución: 0.0519 segundos