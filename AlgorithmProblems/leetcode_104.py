# 104. Maximum depth of a binary tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


class Node:
    """Node of a binary tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_depth(root):
    """
    :param root: root node of binary tree
    :return: maximum depth of binary tree (int)
    """
    # if leaf node, return 0
    if not root:
        return 0
    # otherwise return 1 + maximum depth among left or right subtree
    else:
        return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == "__main__":
    # creating tree
    n1, n2,n3, n4, n5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    #           1
    #          / \
    #         2   3
    #        / \
    #       4   5

    print(max_depth(n1))  # should print 3

    n6 = Node(6)
    print(max_depth(n6))  # should print 1
