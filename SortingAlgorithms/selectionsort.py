"""
The selection sort improves on the bubble sort by making only one exchange
for every pass through the list. In order to do this, a selection sort looks
for the largest value as it makes a pass and, after completing the pass, places it
in the proper location. As with a bubble sort, after the first pass, the largest
item is in the correct place. After the second pass, the next largest is in place.

This process continues and requires n−1 passes to sort n items, since the final item
must be in place after the (n−1) st pass.

Selection sort makes the same number of comparisons as the bubble sort and is
therefore also O(n2). However, due to the reduction in the number of exchanges, the
selection sort typically executes faster in benchmark studies.

Source: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
"""


def selection_sort(arr):

    for numpass in range(len(arr)):
        # assume max value is at index 0
        max_idx = 0
        # start from index 1
        idx = 1
        # keep track of max index by comparing the item at the current
        # index  with the item at max index and updating max_idx.
        while idx < len(arr)-numpass-1:

            if arr[idx] > arr[max_idx]:
                max_idx = idx

            idx += 1

        # swap items at max_idx and the last unsorted idx
        temp = arr[max_idx]
        arr[max_idx] = arr[idx]
        arr[idx] = temp

    return arr


if __name__ == "__main__":
    lst = [2, 34, 11, 22, -4, 5, 0, 3]
    print(selection_sort(lst))
