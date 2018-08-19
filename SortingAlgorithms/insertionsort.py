"""
The insertion sort, although still O(n2), works in a slightly different way.
It always maintains a sorted sublist in the lower positions of the list.
Each new item is then “inserted” back into the previous sublist such that
the sorted sublist is one item larger.

We begin by assuming that a list with one item (position 0) is already sorted.
On each pass, one for each item 1 through n−1, the current item is checked against
those in the already sorted sublist. As we look back into the already sorted sublist,
we shift those items that are greater to the right. When we reach a smaller item or
the end of the sublist, the current item can be inserted.

The maximum number of comparisons for an insertion sort is the sum of the first n−1 integers.
Again, this is O(n2). However, in the best case, only one comparison needs to be done on each pass.
This would be the case for an already sorted list.

One note about shifting versus exchanging is also important. In general, a shift operation
requires approximately a third of the processing work of an exchange since only one assignment is performed.
In benchmark studies, insertion sort will show very good performance.

Source:
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
"""


def insertion_sort(arr):
    # Start from index 1
    for index in range(1, len(arr)):
        # keep track of value at current index
        current_value = arr[index]
        position = index

        # If item at previous position is larger, shift it to
        # the current position and repeat this process until
        # all items at previous positions are larger than current value
        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position = position - 1

        # Once all larger values are shifted, put the
        # current value at the vacant position
        arr[position] = current_value

    return arr


if __name__ == "__main__":
    lst = [2, 34, 11, 22, -4, 5, 0, 3]
    print(insertion_sort(lst))
