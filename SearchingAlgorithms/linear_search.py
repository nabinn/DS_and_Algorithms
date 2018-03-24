def sequential_search(numbers_list, item):
    """
    Returns whether the item is present on the number_list

    O(n)
    """
    found = False
    position = 0

    while position < len(numbers_list) and not found:
        if numbers_list[position] == item:
            found = True

        position += 1

    return found


def ordered_sequential_search(number_list, item):
    """Returns whether an item is present in ordered list
    Has slight advantage if item is not present because we only
    need to check numbers <= item others can be skipped.
    """
    pos = 0
    stop = False
    found = False

    while not found and not stop and pos < len(number_list):
        if number_list[pos] == item:
            found = True
        else:
            if number_list[pos] > item:
                stop = True
            else:
                pos += 1

    return found


if __name__ == "__main__":
    test_list = [2, 4, 5, 6, 7, 89, -2, 0]
    print(sequential_search(test_list, 9))
    print(sequential_search(test_list, -2))

    test_list2 = [-34, -8, 0, 23, 56, 78, 100]
    print(ordered_sequential_search(test_list2, 23))
    print(ordered_sequential_search(test_list2, 101))
