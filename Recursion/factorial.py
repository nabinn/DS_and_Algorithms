
def factorial(n):
    """calculates factorial of a number recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(0))
