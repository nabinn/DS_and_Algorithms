
def factorial(n):
    """calculates factorial of a number recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def tail_factorial(n, accumulator=1):
    """Tail recursive factorial"""
    if n <= 0:
        return accumulator
    else:
        return tail_factorial(n-1, accumulator * n)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(4))
    print(factorial(0))

    print(tail_factorial(5))
    print(tail_factorial(4))
    print(tail_factorial(0))
