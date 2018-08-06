# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def has_cycle(head):
    """
    :param head: Node (head of linked list
    :return: boolean
    ====================
    Naive approach. A set is maintained to keep track of visited nodes.
    If the current node is already present in the visited set, the
    linked list is cyclic. If it reaches the end without encountering
    previously visited nodes,there is no cycle.

    Time Complexity = O(n)
    Space Complexity = O(n)
    where n = number of items in the linked list
    """
    visited_nodes = set()
    current_node = head
    while current_node:
        if current_node in visited_nodes:
            return True
        else:
            visited_nodes.add(current_node)
        current_node = current_node.next
    return False


def has_cycle2(head):
    """
    :param head: Node
    :return: boolean
    =====================
    Better solution with O(1) space complexity.
    It has two pointers: slow and fast.
        - slow traverses 1 node at a time.
        - fast traverses 2 nodes at a time.
    If fast reaches the end of linked list, there are no cycles.
    If the fast pointer ultimately catches up with the slow pointer,
    the linked list is cyclic.

    Time complexity = O(n)
    Space complexity = O(1)
    """
    # if there are less than 2 nodes, no cycle
    if not head or not head.next:
        return False
    else:
        # assign first two nodes as starting points for slow and fast
        slow = head
        fast = head.next

        # repeat until fast catches slow
        while fast != slow:
            # if fast reaches end, return (no cycles)
            if fast is None or fast.next is None:
                return False
            else:
                # Otherwise update the pointers
                slow = slow.next
                fast = fast.next.next

        # If code reaches here, that means fast catches slow.
        # Hence there must be cycle. Thus, return True.
        return True


if __name__ == "__main__":

    # cyclic linked list
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    print(has_cycle(n1))  # True
    print(has_cycle2(n1))  # True

    # non-cyclic linked list
    n5, n6, n7, n8 = Node(5), Node(6), Node(7), Node(8)
    n5.next = n6
    n6.next = n7
    n7.next = n8
    print(has_cycle(n5))  # False
    print(has_cycle2(n5))  # False
