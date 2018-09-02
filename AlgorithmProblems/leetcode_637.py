# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root, level, sums, num_nodes):
    """
    :param root: root node of tree
    :param level: level of node
    :param sums: array containing sum of values for each level
    :param num_nodes: array containing number of nodes for each level
    :return: None (modifies the arrays 'sums' and 'num_nodes'

    ==========================================================
    DFS based approach:

    Two arrays are maintained:
        1. sums => holds sum of values in each level of binary tree
        2. num_nodes => holds the count of number of nodes in each level

    Recursively traverse the tree starting from root.
    For each node N on level L:
        => add N.val to sums[L]
        => add 1 to num_nodes[L]
    """
    if not root:
        return

    if level < len(sums):
        sums[level] += root.val
        num_nodes[level] += 1
    else:
        sums.append(root.val)
        num_nodes.append(1)

    dfs(root.left, level+1, sums, num_nodes)
    dfs(root.right, level+1, sums, num_nodes)


def level_averages1(root):
    """
    :param root: root of binary search tree
    :return: average val for each level of the tree
    ================================================
    This solution uses dfs algorithm.
    Time Complexity: O(N)    N => number of nodes in tree
    Space Complexity: O(h)   h => number of levels in the tree
    """
    sum_arr = []        # array to hold sum of values for each level
    num_nodes_arr = []  # array to hold number of nodes for each level

    dfs(root, 0, sum_arr, num_nodes_arr)

    level_avg = []
    idx = 0
    while idx < len(sum_arr):
        level_avg.append(sum_arr[idx] / num_nodes_arr[idx])
        idx += 1

    return level_avg


def level_averages2(root):
    """BFS based solution
    :param root: root node
    :return: average val for each level of tree
    =============================================
    Algorithm:

        Put root node to queue

        While there are items in queue:
            sum_level, nodes_level = 0, 0

            while queue is not empty:
                Pop first node from queue
                Update summation and count of nodes
                Place the children nodes in temp_queue

            Once the queue is exhaustedFind find average for this level
            using sum_level and nodes_level

            assign temp_queue to queue for the next level

    Complexity Analysis:
        Time:  O(N)   n=> Number of nodes in tree
        Space: O(m)   m => size of queue or temp_queue
                            ie.maximum number of nodes at any level
    """
    level_avg = []  # stores result
    queue = [root]  # using list as queue

    while queue:

        # variables to store sum and num nodes for each level
        sum_of_vals, num_nodes = 0, 0

        # temp queue to hold child nodes in each level
        temp_queue = []

        while queue:
            # pop first node from queue
            node = queue.pop(0)

            # update variables
            sum_of_vals += node.val
            num_nodes += 1

            # if this node has children put them in temp_queue
            if node.left:
                temp_queue.append(node.left)

            if node.right:
                temp_queue.append(node.right)

        # once the queue is empty, update entry for this level
        # and update queue as temp_queue
        level_avg.append(sum_of_vals/num_nodes)
        queue = temp_queue

    return level_avg


if __name__ == "__main__":

    # Test Case 1
    #     3
    #    / \
    #   9   20
    #      /  \
    #    15    7

    n1, n2, n3, n4, n5 = Node(3), Node(9), Node(20), Node(15), Node(7)
    n1.left, n1.right = n2, n3
    n3.left, n3.right = n4, n5

    print(level_averages1(n1))  # [ 3, 14.5, 11]
    print(level_averages2(n1))  # [ 3, 14.5, 11]

    # Test Case 2
    #     5
    #    / \
    #   15  20
    #  /     \
    # 3       5

    root = Node(5)
    root.left, root.right = Node(15), Node(20)
    root.left.left = Node(3)
    root.right.right = Node(5)

    print(level_averages1(root))  # [ 5, 17.5, 4]
    print(level_averages2(root))  # [ 5, 17.5, 4]
