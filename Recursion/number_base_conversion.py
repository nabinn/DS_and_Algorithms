
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
        return base_conversion(n//base, base) + num_str[n % base]


if __name__ == "__main__":
    num = 32
    print(base_conversion(num, 2))  # converting to binary
    print(base_conversion(num, 8))  # converting to octal
    print(base_conversion(num, 16))  # to hexadecimal
