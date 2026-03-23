# Genera 200 números aleatorios de 12 cifras
# Determina cuáles de ellos son números primos
# Aprovecha el paralelismo
# Genera un informe final con:
#     Cuáles de ellos eran primos
#     Tiempo total de ejecución

import threading
import time
import random
import queue

cola = queue.Queue(maxsize=50)

def es_primo(n):
    if n < 2:
        return False

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    return sieve[n]

def productor():


def consumidor():

    