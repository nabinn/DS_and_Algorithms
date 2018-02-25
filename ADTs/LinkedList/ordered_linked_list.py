from linked_list import LinkedList
from simple_node import Node


class OrderedList(LinkedList):
    """
    Special case of linked list where items of the list are ordered.
    Assumes that the data items can be compared to each other.

    All implementations are similar to unordered linked list
    except add and search. So, it inherits from LinkedList class.

    Note: Since the items are guaranteed to be in order, inserting an
    item at a particular index does not make sense now.
    """

    def __init__(self):
        super().__init__()

    def add(self, item):
        """adds the new data to the appropriate position
        based on its value
        """
        new_node = Node(item)  # create node with the data
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            previous = None
            stop = False
            while current is not None and not stop:
                if current.get_data() > item:
                    stop = True
                else:
                    previous = current
                    current = current.get_next()

            if previous is None:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                new_node.set_next(current)
                previous.set_next(new_node)

    def search(self, item):
        """Only search till the current item is less or equal to
        the item we are searching for"""
        found = False
        stop = False
        current = self.head
        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                stop = True
            else:
                current = current.get_next()

        return found


if __name__ == "__main__":
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(-54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(54))
    print(my_list)
