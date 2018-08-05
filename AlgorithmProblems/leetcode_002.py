# 002. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/description/


class ListNode:
    """Node for a singly linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None


# method to add two numbers represented as linked list
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        ==========
        Idea:
        1. Push the numbers from the linked lists to stacks
        2. Initialize resulting sum to zero.
        3. Pop the numbers back from the stacks and multiply them by
        corresponding power of ten and add to the resulting sum.
        4. Once there is a resulting sum, extract individual digits from
        it and create the resulting linked list.
        5. return the resulting linked list.
        """

        # Initialize empty stacks
        stack1, stack2 = [], []  # using list as stack (top => last element)
        result = 0 # variable for resulting summation

        # Traverse linked list and add items to stack
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        # pop digits back from stack and add to result
        while stack1:
            power = len(stack1)-1
            result += stack1.pop()*(10**power)

        while stack2:
            power = len(stack2)-1
            result += stack2.pop()*(10**power)

        # Now create linked list using digits from result
        # First create head node, and keep linking upcoming nodes
        head = ListNode(result % 10)  # head has least significant digit
        result = result // 10  # remove least significant digit from the sum

        current_node = head
        while result > 0:
            current_node.next = ListNode(result % 10)
            result = result // 10
            current_node = current_node.next
        # return the head of the resultant linked list
        return head


def print_llist(lst):
    """Prints linked list in readable format"""
    result = str(lst.val)
    while lst.next:
        lst = lst.next
        result += "->"+str(lst.val)

    print(result)


if __name__ == "__main__":
    # Example
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    # Explanation: 342 + 465 = 807

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l1_plus_l2 = addTwoNumbers(l1, l2)

    print_llist(l1)  # 2 -> 4 -> 3
    print_llist(l2)  # 5 -> 6 -> 4
    print_llist(l1_plus_l2)  # 7 -> 0 -> 8
