# 876. Middle of the linked list
# https://leetcode.com/problems/middle-of-the-linked-list/description/


class Node:
    """Node of a singly linked list.
    Each node has a value and a pointer to next node.
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(lst):
    """creates a linked list using values in a list
    and returns head node
    """
    head = Node(lst[0])
    current = head

    for item in lst[1:]:
        current.next = Node(item)
        current = current.next

    return head


def print_linked_list(head):
    """prints a linked list in the following format:
        node1.val -> node2.val -> node3.val ...
    """
    result = str(head.val)
    current = head
    while current.next:
        current = current.next
        result += " -> " + str(current.val)

    print(result)


def get_middle_node(head):
    """
    :param head: first node of a linked list
    :return: middle node of the linked list
    ======================================
    Two pass solution:
    1st pass: traverses the linked list and count the number of nodes.
    2nd pass: start from head, traverse n/2 nodes(n = total number of nodes)
              and return it.
    Time complexity: O(N)
    Space complexity: O(1)
    """
    num_nodes = 1
    current_node = head

    while current_node.next:
        num_nodes += 1
        current_node = current_node.next

    current_node = head
    for i in range(num_nodes//2):
        current_node = current_node.next

    return current_node


def get_middle_node2(head):
    """
    :param head: head of singly linked list
    :return: node at the middle of linked list
    ================================
    One pass solution:
    Traverse the nodes of the linked list and store then in array.
    Then return the node at the middle index of the array

    Time complexity: O(N)
    Space complexity: O(N)
    """
    lst = [head]
    while lst[-1].next:
        lst.append(lst[-1].next)

    return lst[len(lst)//2]


def get_middle_node3(head):
    """
    :param head: head node of singly linked list
    :return: middle node of the linked list
    ===================================
    One Pass solution:
    Maintain two pointers: slow and fast.
    The fast pointer moves twice fast as that of slow
    When the fast pointer reaches the end of the linked list,
    the slow pointer would be at the middle position.

    Time complexity: O(N)
    Space complexity: O(1)

    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':

    # Test case 1
    linked_list1 = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(linked_list1)  # 1 -> 2 -> 3 -> 4 -> 5

    print_linked_list(get_middle_node(linked_list1))  # 3 -> 4 -> 5
    print_linked_list(get_middle_node2(linked_list1))  # 3 -> 4 -> 5
    print_linked_list(get_middle_node3(linked_list1))  # 3 -> 4 -> 5

    # Test case 2
    linked_list1 = create_linked_list([1, 2, 3, 4, 5, 6])
    print_linked_list(linked_list1)  # 1 -> 2 -> 3 -> 4 -> 5 -> 6

    print_linked_list(get_middle_node(linked_list1))  # 4 -> 5 -> 6
    print_linked_list(get_middle_node2(linked_list1))  # 4 -> 5 -> 6
    print_linked_list(get_middle_node3(linked_list1))  # 4 -> 5 -> 6
