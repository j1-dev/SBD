import numpy as np
from datetime import datetime as dt

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

array = np.random.rand(5000)
now = dt.now()
bubble_sort(array)
then = dt.now()

print(then-now)