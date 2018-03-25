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


def recursive_binary_search_v2(num_list, item):
    """alternate version of recursive binary search.
    This invokes rec_bin_search() which does the actual work.
    """

    def rec_bin_search(number_list, key, low, high):
        if low > high:
            return False
        else:
            mid = (low + high) // 2

            if number_list[mid] == key:
                return True
            else:
                if key > number_list[mid]:
                    return rec_bin_search(number_list, key, mid + 1, high)
                else:
                    return rec_bin_search(number_list, key, low, mid - 1)

    return rec_bin_search(num_list, item, 0, len(num_list)-1)


if __name__ == "__main__":
    list_of_numbers = [-34, -8, 0, 23, 50, 56, 78, 100]

    print(binary_search(list_of_numbers, 23))
    print(binary_search(list_of_numbers, 101))

    print(recursive_binary_search(list_of_numbers, 23))
    print(recursive_binary_search(list_of_numbers, 101))

    print(recursive_binary_search_v2(list_of_numbers, 23))
    print(recursive_binary_search_v2(list_of_numbers, 101))