# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/


def find_pair_1(integer_array, sum_value):
    """
    Naive Solution:
    Consider every pair in the array and return if given sum is found
    Time complexity: O(n2)
    """

    for i in range(0, len(integer_array) - 1):
        for j in range(i+1, len(integer_array)):
            if integer_array[i] + integer_array[j] == sum_value:
                print(f"pair found at indices {i} and {j} of the array {integer_array}")
                return


def find_pair_2(integer_array, sum_value):
    """
    O(n log n) solution using sorting.

    Algorithm:
    1. Sort the array in ascending order. SortingAlgorithms is O (n log n).
    2. Add the elements at start and end of the array.
        If this sum is:
        - equal to required sum, return start and end indices
        - less than the required sum, increment start by 1
        - greater than the required sum, decrement end by 1

    """

    integer_array = sorted(integer_array)  # sorted gives a new array
    # integer_array.sort()  # sort() sorts the array in place
    low = 0
    high = len(integer_array)-1

    # This loop takes O(log n), similar to binary search
    # So, overall complexity = O ((n+1)log n) = O (n log n)
    while low < high:
        low_plus_high = integer_array[low] + integer_array[high]

        if low_plus_high == sum_value:
            print(f"pair found at indices {low} and {high} of the array {integer_array}")
            return
            # if we want to print all the indices pairs, we need to remove the return statement.
            # In that case, we need to increment low and decrement high to avoid infinite loop.
            # low += 1
            # high -= 1

        elif low_plus_high < sum_value:
            low += 1
        else:
            high -= 1


def find_pair_3(integer_array, sum_value):
    """
    O(n) i.e. linear solution using dictionary.

    Algorithm:
    1. Create a dictionary.
    2. Go through each item of the array.
        - If (sum - item) is present in dictionary, return
        - otherwise, put the item in dictionary
    """
    pair_map = {}

    for i in range(len(integer_array)):
        search_key = sum_value - integer_array[i]
        if search_key in pair_map:
            print(f"pair found at indices {pair_map[search_key]}  and {i} of the array {integer_array}")
            return
        else:
            pair_map[integer_array[i]] = i


if __name__ == "__main__":
    arr = [4, 9, 8, 7, 2, 1, 5, 6]
    sum_val = 12

    # find_pair_1(arr, sum_val)
    # find_pair_2(arr, sum_val)
    find_pair_3(arr, sum_val)


