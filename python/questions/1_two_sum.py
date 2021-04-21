# 1. Two Sum - Easy
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    # Time complexity O(N^2) because it loops through the list for each element
    # Space complexity O(1) because no values are being stored
    # We check every combination of x and y, and compare the sum of (x+y) to the target. If it's a match we return the indexes
    def two_sum_naive(self, nums, target):
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]

    # Time complexity O(N)
    # 2. for each element we check to see if the difference from the
    # target exists and that it is not the same as the index
    def two_sum(self, nums, target):
        for x in range(0, len(nums)):
            diff = target - nums[x]
            if diff in nums and x != nums.index(diff):  # the difference is not the same as index
                return [x, nums.index(diff)]

    # one hash pass solution,
    # Time Complexity O(N) - much faster in run time but still
    # Space complexity O(N)Trade off is that we have to save the diff value, trading space for time.
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                diff = target - num
                dic[diff] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 17
    ret = Solution.two_sum(0, nums, target)
    print(ret)
