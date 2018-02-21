from stack import Stack


def reverse_string(input_string):
    result = ""
    s = Stack()
    # push characters of string to stack
    for ch in input_string:
        s.push(ch)
    # pop characters from stack and append to result
    while not s.is_empty():
        result += s.pop()
    return result


if __name__ == '__main__':
    my_string = "apple1235"
    print(f"reverse of {my_string} is {reverse_string(my_string)}")
