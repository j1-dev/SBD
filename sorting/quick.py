import numpy as np
from datetime import datetime as dt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

array = np.random.rand(5000)
now = dt.now()
quick_sort(array)
then = dt.now()

print(then-now)