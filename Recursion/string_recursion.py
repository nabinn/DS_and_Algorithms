def rev_str(input_str):
    """takes a string and returns the reverse string"""
    if len(input_str) == 1:
        return input_str
    else:
        return rev_str(input_str[1:]) + input_str[0]


if __name__ == '__main__':
    print(rev_str("hello"))
