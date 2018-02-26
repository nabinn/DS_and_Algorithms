def rev_str(input_str):
    """takes a string and returns the reverse string"""
    if len(input_str) == 1:
        return input_str
    else:
        return rev_str(input_str[1:]) + input_str[0]


def is_palindrome(input_string):
    """Returns whether the input string is a palindrome.
    This method first removes spaces and special characters
    in the input string and calls the inner method
    _is_palindrome() which in turn does the actual work.
    """

    def _is_palindrome(input_str, start, end):
        """Returns whether a string is a palindrome  or not
        using recursion. Assumes string is not empty.
        """
        if start >= end:
            return True
        if input_str[start] != input_str[end]:
            return False
        else:
            return _is_palindrome(input_str, start + 1, end - 1)

    # remove spaces and special characters and convert to lower case
    input_string = ''.join(ch for ch in input_string if ch.isalnum()).lower()

    return _is_palindrome(input_string, 0, len(input_string) - 1)


if __name__ == '__main__':
    # print(rev_str("hello"))

    input_strings = ["kayak",
                     "aibohphobia",
                     "Live not on evil",
                     "Reviled did I live, said I, as evil I did deliver",
                     "Go hang a salami; I’m a lasagna hog.",
                     "Able was I ere I saw Elba",
                     "Kanakanak",
                     "Wassamassaw",
                     "states",
                     "google",
                     "test"
                     ]
    for item in input_strings:
        print(is_palindrome(item))
