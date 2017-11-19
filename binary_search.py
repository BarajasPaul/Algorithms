#!/bin/python3.6
"""simple binary search"""

def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = my_list[middle]
        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None

def recursive_binary_search()

LIST = [1, 3, 5, 7, 9, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
print(binary_search(LIST, 5))
