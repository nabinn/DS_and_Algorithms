# 341. Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
# Note:
# This implementation makes use of interface provided in the question
# See above link for more information.


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = self._create_stack(nestedList)

    def _create_stack(self, lst):
        """Reverses the lst and returns it"""
        result = []
        for idx in range(len(lst) - 1, -1, -1):
            result.append(lst[idx])
        return result

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            # peek the top element of stack
            top = self.stack[-1]

            # if top of stack is Integer return True
            if top.isInteger():
                return True
            # if top of stack is a list, remove it from the stack and
            # push items from it back to the stack
            self.stack = self.stack[:-1] + self._create_stack(top.getList())
        return False
