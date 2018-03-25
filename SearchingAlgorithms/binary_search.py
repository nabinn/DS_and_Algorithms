def binary_search(num_list, item):
    """
    :param num_list: sorted list of numbers
    :param item: item to search
    :return: boolean found

    This takes O(log n)
    """

    low = 0
    high = len(num_list) - 1
    found = False

    while low <= high and not found:

        mid = (low + high) // 2

        if item == num_list[mid]:
            found = True

        elif item > num_list[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return found


def recursive_binary_search(num_list, item):
    if len(num_list) == 0:
        return False
    else:
        mid = len(num_list) // 2
        if item == num_list[mid]:
            return True

        else:
            if item > num_list[mid]:
                return recursive_binary_search(num_list[mid + 1:], item)
            else:
                return recursive_binary_search(num_list[:mid], item)



if __name__ == "__main__":
    test_list2 = [-34, -8, 0, 23, 50, 56, 78, 100]
    # print(binary_search(test_list2, 23))
    # print(binary_search(test_list2, 101))

    print(recursive_binary_search(test_list2, 23))
    print(recursive_binary_search(test_list2, 101))
