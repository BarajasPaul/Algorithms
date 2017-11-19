#!/bin/ṕython3.6
"""recursive practice"""

import time

def sum(array):
    if array:
        return array[0] + sum(array[1:])
    return 0

def count(array):
    if array:
        return 1 + count(array[1:])
    return 0

def max(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_array = max(array[1:])
    return array[0] if array[0] > sub_array else sub_array


STARTIME = time.time()
print(max([1, 5, 3, 3434, 543654, 2, 3434, 54, 545, 99, 1]))
print("--- %s seconds ---" % (time.time() - STARTIME))
