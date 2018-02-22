from stack import Stack


def infix_to_postfix(infix_expression):
    """
    :param infix_expression: string  eg: (A+B)*C-D
    :return: postfix expression: string eg: AB+C*D-

    Algorithm: (borrowed from http://interactivepython.org)

    Assume the infix expression is a string of tokens delimited by spaces.
    The operator tokens are *, /, +, and -, along with the left and right
    parentheses, ( and ). The operand tokens are integers or single-character
    identifiers A, B, C, and so on.

    The following steps will produce a string of tokens in postfix order.
    1.Create an empty stack called opstack for keeping operators.
        Create an empty list (or string)for output.
    2.Convert the input infix string to a list by using the string method split.
    3.Scan the token list from left to right.
        a.If the token is an operand, append it to the end of the output list.
        b.If the token is a left parenthesis, push it on the opstack.
        c.If the token is a right parenthesis, pop the opstack until the corresponding
            left parenthesis is removed. Append each operator to the end of the output list.
        d.If the token is an operator, *, /, +, or -, push it on the opstack. However,
            first remove any operators already on the opstack that have higher or
            equal precedence and append them to the output list.
    4.When the input expression has been completely processed, check the opstack.
    Any operators still on the stack can be removed and appended to the end of the output list.
    """
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    operands += operands.lower()  # all alphabets are operands
    # operator precedence mapping
    operators = {
        "(": 1,
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "%": 3,
        "^": 4
    }
    opstack = Stack()
    postfix_list = []
    infix_list = infix_expression.split()

    for token in infix_list:
        if token in operands or token.isnumeric():
            postfix_list.append(token)

        elif token == "(":
            opstack.push(token)

        elif token == ")":
            top = opstack.pop()
            while top != "(":
                postfix_list.append(top)
                top = opstack.pop()

        elif token in operators:
            while (not opstack.is_empty() )and \
                    operators[opstack.peek()] >= operators[token]:
                postfix_list.append(opstack.pop())
            opstack.push(token)
        else:
            continue

    while not opstack.is_empty():
        postfix_list.append(opstack.pop())

    return " ".join(postfix_list)


if __name__ == "__main__":
    print(infix_to_postfix("5 * 3 ^ ( 4 - 2 ) "))  # 5 3 4 2 - ^ *
    print(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"))  # 10 3 5 * 16 4 - / +
    print(infix_to_postfix("( A + B ) * C - D"))  # A B + C * D -
    print(infix_to_postfix("A * B + C * D"))  # A B * C D * +
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    # A B + C * D E - F G + * -
    print(infix_to_postfix(" a + b * ( c ^ d - e ) ^ ( f  + g * h ) - i "))
    # a b c d ^ e - f g h * + ^ * + i -



