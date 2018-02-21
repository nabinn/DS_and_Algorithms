"""
Creating list and checking time
"""
from timeit import Timer


def create_list1():
    """creating list by concatenation"""
    lst = []
    for i in range(1000):
        lst = lst + [i]


def create_list2():
    """creating list by appending"""
    lst = []
    for i in range(1000):
        lst.append(i)


def create_list3():
    """using list comprehension"""
    lst = [i for i in range(1000)]


def create_list4():
    """passing range function to list constructor"""
    lst = list(range(1000))


def check_time():
    t1 = Timer("create_list1()", "from __main__ import create_list1")
    print("concat: ", t1.timeit(number=1000), "milliseconds")

    t2 = Timer("create_list2()", "from __main__ import create_list2")
    print("append: ", t2.timeit(number=1000), "milliseconds")

    t3 = Timer("create_list3()", "from __main__ import create_list3")
    print("comprehension: ", t3.timeit(number=1000), "milliseconds")

    t4 = Timer("create_list4()", "from __main__ import create_list4")
    print("list range: ", t4.timeit(number=1000), "milliseconds")


if __name__ == '__main__':
    check_time()
