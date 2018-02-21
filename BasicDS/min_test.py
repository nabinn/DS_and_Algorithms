"""
Finding min value in a list 
a. quadratic time
b. linear time
"""

import time
from random import randrange


def find_min_linear(lst):
    """finding min in linear time"""
    current_min = lst[0]
    for item in lst:
        if item < current_min:
            current_min = item
    return current_min


def find_min_quad(lst):
    """min function with quadratic time complexity"""
    overall_min = lst[0]
    for i in lst:
        is_smallest = True
        for j in lst:
            if i > j:
                is_smallest = False
        if is_smallest:
            overall_min = i
    return overall_min


def measure_time(min_function):
    """using 10 list sizes from 1,000 to 10,000"""
    for list_size in range(1000, 10001, 1000):
        # create a list with random numbers
        lst = [randrange(1000000) for x in range(list_size)]
        start = time.time()
        min_function(lst)
        end = time.time()
        print("list size:  %d time: %f sec" % (list_size, end - start))


if __name__ == '__main__':
    print("min function with quadratic time ")
    measure_time(find_min_quad)
    print("---------------")
    print("min function with linear time ")
    measure_time(find_min_linear)
