"""Evaluation of an expression in postfix format using stack"""
from stack import Stack


def do_operation(operator, op1, op2):
    if operator == "*":
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    elif operator == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfix_eval(postfix_expr):
    """
    :param postfix_expr: String in postfix format
    :return: result of evaluation
    Assume the postfix expression is a string of tokens delimited by spaces.
    The operators are *, /, +, and - and the operands are assumed to be single-digit
    integer values. The output will be an integer result.

    1.Create an empty stack called operandStack.
    2.Convert the string to a list by using the string method split.
    3.Scan the token list from left to right.
        a. If the token is an operand, convert it from a string to an integer
            and push the value onto the operandStack.
        b. If the token is an operator, *, /, +, or -, it will need two operands.
            Pop the operandStack twice. The first pop is the second operand and
            the second pop is the first operand. Perform the arithmetic operation.
            Push the result back on the operandStack.
    When the input expression has been completely processed, the result is on the stack.
    Pop the operandStack and return the value.
    """
    operand_stack = Stack()
    postfix_list = postfix_expr.split()
    operands = "0123456789"
    operators = "+-*/"
    for token in postfix_list:
        if token in operands:
            operand_stack.push(int(token))

        elif token in operators:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            operand_stack.push(do_operation(token,operand1, operand2))
        else:
            continue

    return operand_stack.pop()


if __name__ == "__main__":

    print(postfix_eval('7 8 + 3 2 + /'))  # 3.0
