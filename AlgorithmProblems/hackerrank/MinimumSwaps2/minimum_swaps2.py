# Minimum Swaps 2
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def get_minimum_swaps(arr):
    """
    :param arr: unsorted array containing unique integers
    :return: int (minimum number of swaps required to sort the array
    =============================================================
    Algorithm:
     - Save a sorted array as a new variable (this acts as reference).
     - Maintain an index-map for quick index lookup for a value in the array.
     - Initialize swap counter to zero.
     - Iterate through the unsorted array:
        - if numbers at a given index match in both sorted and original array => skip
        - otherwise (if they do not match):
                - find the index of the actual number that should be in this position
                    (using sorted array and the index-map as references)
                - swap the current number with this number and update the index-map accordingly.
                - increment swap counter
    - Return swap counter
    """
    sorted_array = sorted(arr)

    # creating index-map for the unsorted array
    # Assuming all values in the unsorted array are unique
    index_map = {value: index for index, value in enumerate(arr)}

    swap_counter = 0

    for idx, num in enumerate(arr):
        # the actual number that should be at this index
        correct_value = sorted_array[idx]

        if num != correct_value:

            # get the index of the correct value
            swap_index = index_map[correct_value]

            # swap current number with the number at that index
            arr[idx], arr[swap_index] = arr[swap_index], arr[idx]

            # update index-map
            index_map[num] = swap_index
            index_map[correct_value] = idx

            # increment swap counter
            swap_counter += 1

    return swap_counter


if __name__ == "__main__":
    arr1 = [7, 1, 3, 2, 4, 5, 6]
    arr2 = [4, 3, 1, 2]
    arr3 = [2, 3, 4, 1, 5]
    arr4 = [1, 3, 5, 2, 4, 6, 8]

    # should print 5 3 3 3
    for array in [arr1, arr2, arr3, arr4]:
        print(get_minimum_swaps(array), end="\t")
