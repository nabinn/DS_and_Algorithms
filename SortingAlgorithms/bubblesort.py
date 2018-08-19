"""
The bubble sort makes multiple passes through a list.
It compares adjacent items and exchanges those that are out of order.
Each pass through the list places the next largest value in its proper place.
In essence, each item “bubbles” up to the location where it belongs.

Source:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
"""


def bubble_sort(arr):
    """
    :param arr: an unsorted array
    :return: sorted array
    =========================
    Time complexity: O(N2)
    Space complexity: O(1)
    """
    # number of passes = length of the array
    for numpass in range(len(arr)):
        # In each pass compare two adjacent items and swap them if necessary.
        # In each pass, one of the item is sorted.
        # So, loop only compare upto unsorted index.
        for i in range(0, len(arr)-numpass-1):
            # sorting in ascending order
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


if __name__ == "__main__":
    lst = [2, 34, 11, 22, -4, 5, 0, 3]
    print(bubble_sort(lst))
