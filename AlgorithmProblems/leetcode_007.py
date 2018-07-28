 # Link to the problem: 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/description/


def reverse_number(x):
    result = 0
    is_positive = 1

    # for 32 bit number
    low = -2 ** 31
    high = 2 ** 31 - 1

    # for negative number
    if x < 0:
        is_positive = -1
        x = -1 * x

    while x != 0:
        result = result * 10 + x % 10

        if result > high or result < low:
            return 0
        x //= 10

    return result * is_positive


def reverse(input_num):
    """
    :type input_num: int
    :rtype: int
    """
    if input_num < 0:
        return -reverse(-input_num)

    result = 0
    while input_num > 0:
        result = result * 10 + input_num % 10
        input_num = input_num // 10

    return result if result <= 0x7fffffff else 0


if __name__ == "__main__":
    print(reverse_number(1))
    print(reverse_number(125))
    print(reverse_number(-1253))
    print(reverse_number(120))
    print(reverse_number(-120))
