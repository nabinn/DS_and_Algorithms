"""
Merge sort is a recursive algorithm that continually splits a list in half.
If the list is empty or has one item, it is sorted by definition (the base case).
If the list has more than one item, we split the list and recursively invoke a
merge sort on both halves.

Once the two halves are sorted, the fundamental operation, called a merge, is performed.
Merging is the process of taking two smaller sorted lists and combining them together
into a single, sorted, new list.

Source:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
"""


def merge(left_array, right_array):
    """Takes in two sorted arrays and merges them such
    that the resultant array is sorted"""
    result = []
    i, j = 0, 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1
    # if the right array is exhausted but
    # left array has some elements left
    while i < len(left_array):
        result.append(left_array[i])
        i += 1

    # if the left array is exhausted but
    # right array has some elements left
    while j < len(right_array):
        result.append(right_array[j])
        j += 1

    return result


def merge_sort(arr):
    """
    :param arr: input array
    :return: sorted array using merge sort

    Complexity analysis:
    This has two phases -
    1. split the array in halves which takes O(log n) time
    2. merging the sorted array which takes O(n) time
    Hence, there are log n splits, each of which costs n for a total of n(log n) operations.
    Thus,it is an O(n log n) algorithm.
    """
    # base case:
    # if there is only one element return it
    if len(arr) < 2:
        return arr
    # otherwise:
    # split the array into 2 from middle
    # apply merge sort on each half and merge them
    else:
        mid_idx = len(arr) // 2
        left_arr = arr[:mid_idx]
        right_arr = arr[mid_idx:]

        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)
        return merge(left_arr, right_arr)


if __name__ == "__main__":
    lst = [2, 34, 11, 22, 4, 5, 0, 1]
    print(merge_sort(lst))
