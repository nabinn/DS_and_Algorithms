# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem


# Note: Using list as Stack:
# stack top <=> last item of list
# Stack operations:
# push(item) <=> list.append(item)
# pop() <=> list.pop()
# peek() <=> list[-1]

def superReducedString(s):
    """
    :param s: input string
    :return: reduced string
    ==========================
    This method takes an input string and returns a reduced string
    without duplicates(i.e. A pair of matching adjacent characters).

    Algorithm:
    1. Create a Stack
    2. Iterate through the characters of s
        a. peek the top of stack and compare it with current character
        If they match => pop the stack
        If they don't match => push current character to stack
    3. If stack is empty, return "Empty String"
    Otherwise return the string by joining the items of stack(list).
    """
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "Empty String" if not stack else "".join(stack)
