#!/bin/python3.6
"""Basic quicksort algorithm"""

def quicksort(array):
    """quicksort code"""

    if len(array) > 1:
        pivot = array[0]
        less = [i for i in array[1:]
                if i <= pivot]

        greater = [i for i in array[1:]
                   if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    return array

ARRAY = [10, 5, 2, 3, 9, 1]

print(quicksort(ARRAY))
