# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
#
# Input: [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1.
#
# Example 2:
#
# Input: [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27.
#

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depth_first_search_sum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # We go through each element in the list, and see if it is a list or an element.
        # if it is an element, we can multiply it by the depth and add it to the sum.
        # if it is a nested list, we have to recursively go into that list and perform the same operations, but with an increased depth
        # for example input = [[1,1],2,[1,1]], has 3 elements. element 1 = nestedList [1,1], element 2 = 2, element 3 = nestedList [1,1].
        # element 2 has a depth of 1, and element 1 and 3 have a depth of 2.
        # example input 2 = [1,[4,[6]]], has 2 elements. element 1 = 1, element 2 = nestedList [4,[6]]. Element 2 itself has 2 elements, element 1(2) = 4, element 2(2) = nestedList [6].
        # even though element 2(2) has a nestedlisted that contains only 1 element, it counts as a deeper list.

        # we are given pre-defined functions that we can use. isInteger checks to see if it's an integer and not a list.
        # getList gives back the nestedList if it is a nestedList
        def dfs(nestedList, depth):
            total = 0
            for element in nestedList:
                if element.isInteger():                                  # checks if it an integer
                    total += element.getInteger() * depth                # since it's an integer, we multiply it by the depth and add it to total
                else:                                                    # else: this means that the element is another nestedList,
                    total += dfs(element.getList(), depth + 1)           # so we have to recursively get the total of that list and then add it to our current total.
                return total                                             # returns the total, even for nestedList totals

        dfs(nestedList, 1)









