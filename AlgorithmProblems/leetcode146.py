# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/description/


class Node:
    """
    Node for a doubly linked list.
    The data is stored in key:value format.
    Each node has pointers to the previous and the next nodes.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :param capacity: the defined capacity of the cache

        This method initializes a doubly linked list with
        two nodes: head and tail, connected to one another.

        A map is also initialized. Given a key, this map is used for
        a constant lookup for the corresponding node in the linked list.
        """
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head

        self.map = {}  # maps a key to the node in the linked list

    def _add(self, node):
        """
        Adds node to the second to the last position
        (i.e. in front of tail) of doubly linked list.
        """
        # get current second last node
        current = self.tail.previous

        # define new set of links
        current.next = node
        node.previous = current

        self.tail.previous = node
        node.next = self.tail

    def _remove(self, node):
        """Removes the node from doubly linked list"""
        previous_node = node.previous
        next_node = node.next

        previous_node.next = next_node
        next_node.previous = previous_node

    def get(self, key):
        """
        Given a key, returns value if present in cache
        otherwise returns -1
        :type key: int
        :rtype: int
        ================
        Idea:
        If the key is present, return its value and mark it as recently used.
        For that, get the corresponding node from the map.Then remove the
        node from its current position  and add it to the second to last
        position of the doubly linked list.

        Otherwise( if key is not present), return -1.
        """
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            self._add(node)

            return node.value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        =====================
        Idea:
        If key is already present, update its value and mark it as recently used
        (i.e. remove node from its current position and add the new node with new value
        at the end(second to last position) of the doubly linked list.

        Otherwise (i.e., if key is not present), add entry to the map and add
        a new node at the end(second to last position) of the doubly linked list.

        After each put operation, check if the size of the cache exceeds capacity.
        If it exceeds then,remove the least recently used node
        (i.e. the node after the head) from the doubly linked list.
        Also, remove this node from the map.
        """

        if key in self.map:
            # get the node
            node = self.map[key]
            # remove it from doubly linked list
            self._remove(node)

        # create a new node
        node = Node(key, value)
        # add to doubly linked list's last position
        self._add(node)

        # add entry to map
        self.map[key] = node

        # if the cache size exceeds capacity, remove the
        # least recently used node from linked list and the map
        if len(self.map) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.map[node.key]


if __name__ == "__main__":
    cache = LRUCache(2)  # capacity = 2
    cache.put(1, 1)
    cache.put(2, 2)
    result1 = cache.get(1)  # returns 1
    cache.put(3, 3)  # evicts key 2
    result2 = cache.get(2)  # returns - 1 (not found)
    cache.put(4, 4)  # evicts key 1
    result3 = cache.get(1)  # returns -1 (not found)
    result4 = cache.get(3)  # returns 3
    result5 = cache.get(4)  # returns 4

    # This print statement should print: 1 -1 -1 3 4
    print(result1, result2, result3, result4, result5)