# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]
#

class Solution(object):

    # naive solution: for each element in the array, find a pair that 'negates' it, e.i. sums it to zero.
    # time complexity: for each element in the array, we essentially do 2sum, so that'd be O(N) * O(N) = O(N^2)
    def three_sum(self, nums):
        for num in nums:
            return 0



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    ret = Solution.three_sum(0, nums)
    print(ret)