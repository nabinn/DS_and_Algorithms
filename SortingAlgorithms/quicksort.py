import random


def quick_sort(arr):
    """ Recursive quick sort algorithm ( returns a sorted array)

    Time complexity: depends on the choice of pivot
    O(n log n) => average/best case
    O(n2) => worst case

    Space complexity: O(n)

    Idea:
     - If there is only one item or no item: return the array as it is
     - Otherwise:
        - Choose first item as pivot.
        - create two arrays
            1. items less than(or equal to) the pivot [lesser]
            2. items greater than the pivot [greater]
        - create new array by placing pivot in between lesser and greater
        - apply quick sort recursively to lesser and greater parts
    """

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


def quicksort(arr):
    """
    This outer function is a helper which calls the
    inner function _quicksort() that does all the work

    :param arr: array of numbers
    :return: sorted array
    """

    def _quicksort(array, left, right):
        """
        Recursive quick sort algorithm without using extra space.
        Performs in-place sorting of the array passed as parameter.

        :param array: array of numbers
        :param left: left pointer
        :param right: right pointer
        :return: None
        """
        if left >= right:
            return

        i, j = left, right

        # choose a random value from the array as pivot
        pivot = array[random.randint(left, right)]

        # loop until left and right pointers meet or cross each other
        while i <= j:
            # keep on incrementing i until a number greater than pivot is found
            while array[i] < pivot:
                i += 1
            # keep on incrementing j until a number greater than pivot is found
            while array[j] > pivot:
                j -= 1

            # once a large number is found on left side and a smaller number
            # is found on the right side, swap these numbers and update indices
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i, j = i+1, j-1

        # Now apply quick sort to lower and upper half recursively
        _quicksort(array, left, j)
        _quicksort(array, i, right)

    # invoking the actual function for quick sort
    _quicksort(arr, 0, len(arr))


if __name__ == "__main__":
    lst1 = [2, 34, 11, 22, -4, 5, 0, 3]
    print(quick_sort(lst1))

    lst2 = [2, 34, 11, 22, -4, 5, 0, 3]
    print(quick_sort(lst2))


