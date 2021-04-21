# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
#
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


class Solution(object):

    # Naive first to mind solution: Add elements of array to a dictionary where the key is the number, and the value is the amount.
    # Then go through the dic and return the key that has a value one 1.
    # Time complexity: O(N) to insert all the numbers into the dictionary, and O(N) to find the number with value == 1
    # we're sacrificing O(N) space complexity to create the hash table.
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] = 2
            else:
                dic[num] = 1

        for element in dic:
            if dic[element] == 1:
                return element
