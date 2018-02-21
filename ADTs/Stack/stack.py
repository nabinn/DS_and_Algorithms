class Stack:
    """
        Stack implementation using list.
        The end of the list is considered top.
        All operations listed below are O(1)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(6)
    s.push('test_str')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(5.5)
    print(s.pop())
    print(s.pop())
    print(s.size())
