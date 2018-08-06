# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :param x: int
        :return: None
        ==================
        Before pushing the item x to stack, compare it with current min,
        and update current min if the item is smaller than current min.
        Then push the tuple (item, current_min) to the stack.
        """
        current_min = self.get_min()
        if not self.stack or x < current_min:
            current_min = x
        self.stack.append((x, current_min))

    def pop(self):
        """
        :return: None
        """
        self.stack.pop()

    def top(self):
        """
        :return: int
        """
        if not self.stack:
            return None
        return self.stack[-1][0]

    def get_min(self):
        """
        :return: int
        """
        if not self.stack:
            return None
        return self.stack[-1][1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    result1 = minStack.get_min()  # Returns - 3
    minStack.pop()
    result2 = minStack.top()  # Returns 0.
    result3 = minStack.get_min()  # Returns - 2

    print(result1, result2, result3)  # should print -3 0 -2
