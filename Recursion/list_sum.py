
def sum_list(lst):
    """calculates the sum of a list of numbers recursively"""

    if len(lst) == 1:  # base case
        return lst[0]
    else:
        return lst[0]+sum_list(lst[1:])


if __name__ == "__main__":
    # my_list = [1, 2, 3, 4, 5]
    my_list = [i for i in range(101)]
    print(sum_list(my_list))
