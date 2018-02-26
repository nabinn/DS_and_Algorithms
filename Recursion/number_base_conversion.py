import sys
sys.path.append('../ADTs/Stack')

from stack import Stack


def base_conversion(n, base):
    """converts a decimal number to any
    base between 2 and 16.
    :param: n(int) is a decimal number
    Returns the converted number as a string.
    """
    num_str = "0123456789ABCDEF"

    if n < base:
        return num_str[n]
    else:
        return base_conversion(n // base, base) + num_str[n % base]


def base_conversion_stack(n, base):
    """converts a decimal number to any base between 2 and 16.
    This implementation makes use of stack instead of recursion.
    :param: n(int) is a decimal number
    Returns the converted number as a string."""
    num_stack = Stack()
    num_str = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            num_stack.push(num_str[n])
        else:
            num_stack.push(num_str[n % base])
        n = n // base
    result = ""
    while not num_stack.is_empty():
        result += num_stack.pop()
    return result


if __name__ == "__main__":
    num = 32
    print(base_conversion(num, 2))  # converting to binary
    print(base_conversion(num, 8))  # converting to octal
    print(base_conversion(num, 16))  # to hexadecimal

    print(base_conversion_stack(num, 2))  # converting to binary
    print(base_conversion_stack(num, 8))  # converting to octal
    print(base_conversion_stack(num, 16))  # to hexadecimal
