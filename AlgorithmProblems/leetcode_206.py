# 206. Reverse Linked List
# ttps://leetcode.com/problems/reverse-linked-list/description/


class Node:
    """Node of a singly linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_linked_list(head):
    """
    :type head: Node (head of input linked list)
    :rtype: Node (head of reversed linked list)
    ===========================

    """
    # if there is no node
    if not head:
        return None

    # if there is one node return it
    if not head.next:
        return head

    else:
        # keep pointer to 3 nodes
        previous_node = None
        current_node = head
        next_node = head.next

        while current_node:
            # change the next pointer of current node to previous node
            current_node.next = previous_node

            # assign current node to previous and next node to current
            previous_node = current_node
            current_node = next_node

            # when there is no next node, head = previous node
            if not next_node:
                head = previous_node
            else:
                # shift next node to its next
                next_node = next_node.next

        return head


###### helper functions ######

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
    """prints a linked list"""
    result = str(head.val)
    current = head
    while current.next:
        current = current.next
        result += " -> " + str(current.val)

    print(result)


######################################

if __name__ == "__main__":
    l1 = create_linked_list([1, 2, 3, 4])
    print_linked_list(l1)  # 1 -> 2 -> 3 -> 4

    l2 = reverse_linked_list(l1)
    print_linked_list(l2)  # 4 -> 3 -> 2 -> 1
