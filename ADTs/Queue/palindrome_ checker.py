"""Palindrome checker using deque
"""
from double_ended_queue import Deque


def palindrome_checker(input_string):
    # convert the string to lowercase
    input_string = input_string.lower()
    dq = Deque()
    match = True
    for ch in input_string:
        # skip empty spaces and insert to queue
        if ch != " ":
            dq.add_front(ch)

    while dq.size() > 1 and match:
        first = dq.remove_front()
        last = dq.remove_rear()
        if first != last:
            match = False

    return match


if __name__ == "__main__":
    print("palindrome or not: ")

    words = ["I did, did I",
             "radar",
             "apple",
             "test str",
             "Eva can I see bees in a cave",
             "No lemon, no melon"]
    for word in words:
        print(f"{word} => {palindrome_checker(word)}")

