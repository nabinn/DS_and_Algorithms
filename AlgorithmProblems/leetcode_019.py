# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


class Node:
    """Node of a singly linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def remove_nth_node(head, n):
    """
    :param head: head Node of singly linked list
    :param n: int
    :return: head of new linked list after removing
            nth node from the end of the list
    ==========================================
    This solution removes the node in only one pass by using 
    two pointers- slow and fast. Fast is ahead of the slow by n nodes.
    """
    # slow and fast both start from head
    slow, fast = head, head

    # move fast pointer to n positions ahead of slow
    for _ in range(n):
        fast = fast.next

    # Since the problem assumes n is valid, fast cannot
    # be None in the middle of the above loop. But it can be
    # None at the end of the loop, if the linked list has exactly
    # n number of nodes. In that case, we need to remove the head
    # of the linked list and return the resulting list.
    if not fast:
        return head.next

    # loop till the end of the list and update pointers
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Now fast has reached the end of the list and
    # slow points to the node at (n+1)th position from the end.
    # So, we need to remove the next node of slow pointer
    slow.next = slow.next.next

    # return the modified list
    return head


######### helper functions ################

def create_linked_list(lst):
    """
    :param lst: a list of numbers
    :return: head of linked list created using numbers of list
    """
    head = Node(lst[0])
    current = head
    for item in lst[1:]:
        current.next = Node(item)
        current = current.next
    return head


def print_linked_list(head):
    """ prints linked list in human readable format
    :param head: head node of linked list
    :return: None
    """
    res = str(head.val)
    current = head

    while current.next:
        current = current.next
        res += " -> "+str(current.val)

    print(res)
##############################################


if __name__ == "__main__":

    # Test case 1
    ll = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(ll)  # 1 -> 2 -> 3 -> 4 -> 5

    result = remove_nth_node(ll, 2)
    # Should print: 1 -> 2 -> 3 -> 5
    print_linked_list(result)

    # Test case 2
    ll2 = create_linked_list([1, 2])
    print_linked_list(ll2)  # 1 -> 2

    result = remove_nth_node(ll2, 2)
    # Should print: 2
    print_linked_list(result)
