import numpy as np
from datetime import datetime as dt

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

array = np.random.rand(5000)
now = dt.now()
insertion_sort(array)
then = dt.now()

print(then-now)