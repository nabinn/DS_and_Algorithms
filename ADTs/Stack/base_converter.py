"""
Conversion from decimal to binary,
octal and hexadecimal format using stack
"""
from stack import Stack


def divide_by_base(num, base):
    """
    params:
        num: int, decimal number
        base: int, the base

    returns:
        result: string in base fromat
    """
    digits = "0123456789ABCDEF"
    s = Stack()
    while num > 0:
        s.push(num % base)
        num = num // base

    result = ""
    while not s.is_empty():
        result += digits[s.pop()]

    return result


if __name__ == '__main__':

    bases = {
        2: "binary",
        16: "hexa",
        8: "octal"
    }

    for dec_num in [1, 9, 5, 7, 10, 16, 25, 256]:
        for base in [2, 8, 16]:
            converted_num = divide_by_base(dec_num, base)
            print(f"decimal: {dec_num} => {bases[base]}:{converted_num}")
