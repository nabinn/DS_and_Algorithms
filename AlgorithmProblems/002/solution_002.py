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
    print(reverse(125))
    print(reverse(-1253))
    print(reverse(120))
    print(reverse(-120))