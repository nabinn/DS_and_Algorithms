from simple_node import Node


class LinkedList:
    """Unordered linked list
    Nodes are linked together as a chain, each node pointing to
    the next node in the list.
    Keeps track of only head (and tail). Other nodes are reached by
    traversing the link starting at the head.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None and self.tail is None

    def add(self, item):
        """adds a new data to the head of the list """
        new_node = Node(item)  # create node with the data
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)  # point its next to the current head
            self.head = new_node  # set the node as the head

    def size(self):
        current_node = self.head
        node_count = 0
        while current_node is not None:
            node_count += 1
            current_node = current_node.get_next()

        return node_count

    def search(self, item):
        found = False
        current_node = self.head
        while current_node is not None and not found:
            if current_node.get_data() == item:
                found = True
            else:
                current_node = current_node.get_next()

        return found

    def remove(self, item):
        """assumes that the item is present in the list"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        # if there was only one node
        if previous is None:
            self.head = current.get_next()
            self.tail = current.get_next()
        elif current.get_data() == self.tail.get_data():
            previous.set_next(None)
            self.tail = previous
        else:
            previous.set_next(current.get_next())

    def append(self, item):
        """appends item to the end of the node"""
        new_node = Node(item)
        self.tail.set_next(new_node)
        self.tail = new_node

    def index(self, item):
        """returns the index of item in the list
        assuming  item is in the list and
        indexing starts from zero
        """
        item_index = 0
        current = self.head
        found = False
        while not found:
            item_index += 1
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return item_index - 1

    def pop(self, pos=None):
        """pops the item from the list
        If index is provided, item is popped from that
        index, otherwise the last item is popped.
        Assumes there is at least one element on the list.
        """
        previous = None
        current = self.head

        # if there is only one item and position is 0 or not provided
        if current.get_next() is None and (pos is None or pos == 0):
            return_value = current.get_data()
            self.head = None
        # if list has more than one element and head has to be removed.
        elif pos == 0:
            return_value = current.get_data()
            self.head = current.get_next()
        else:
            index_reached = False
            current_idx = 0
            while not index_reached:
                previous = current
                current = current.get_next()
                current_idx += 1
                # if "pos" index or the end of the list is reached
                if current_idx == pos or current.get_next() is None:
                    index_reached = True

            return_value = current.get_data()
            previous.set_next(current.get_next()
                              if current.get_next() is not None
                              else None)

        return return_value

    def insert(self, pos, item):
        """ Inserts item at position pos
        Assumes pos is a valid index
        """
        # if pos is zero add to head
        if pos == 0:
            self.add(item)
        else:
            previous = None
            current = self.head
            current_idx = 0
            index_reached = False
            while not index_reached:
                previous = current
                current = current.get_next()
                current_idx += 1
                if current_idx == pos:
                    index_reached = True

            new_node = Node(item)
            new_node.set_next(current)
            previous.set_next(new_node)

    def __str__(self):
        """provides custom string representation of the list"""
        list_str = ""
        current = self.head
        while current is not None:
            list_str += f" => {current.get_data()}"
            current = current.get_next()
        return list_str


if __name__ == "__main__":
    my_list = LinkedList()
    for item in [31, 77, 17, 93, 26, 54, 95]:
        my_list.add(item)

    my_list.remove(31)

    # print(my_list)
    # print(my_list.index(54))
    # print("size =", my_list.size())
    my_list.add(99)
    my_list.append(100)
    print(my_list)
    print(my_list.pop())
    print(my_list)
    print(my_list.pop(0))
    print(my_list.pop(3))
    print(my_list.pop(1))
    print(my_list.pop(3))
    print(my_list)
    my_list.insert(2, 100)
    print(my_list)
