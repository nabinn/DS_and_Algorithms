class Queue():
    """Simple queue implementation using python list.
    Assuming rear is at index 0 and front is at the last 
    index of the list. Hence, in this implementation,
    enqueue is O(n) and dequeue is O(1).
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    print("size:",q.size())
    print("is_empty: ", q.is_empty())
    q.enqueue(5)
    q.enqueue('apple')
    q.enqueue(True)
    print("size: ", q.size())
    print("is_empty: ", q.is_empty())
    q.enqueue(9.3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
