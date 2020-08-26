# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
# Input: [3,0,1]
# Output: 2
#
# Example 2:
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


class Solution(object):

    # Naive solution: Sort the nums go through the set 1 -> length, and see if the current number is 1 greater than previous. if not, previous number is missing
    # Time complexity O(N), goes through array once
    # Space complexity O(N), size of set depends on nums
    # this does not handle a few edge cases, such as [0], [1], [0,1,2,3] (missing 4)
    def missingNumber(self, nums):
        nums.sort()
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1] + 1:
                return (nums[x] - 1)

    # this one is the expected sum of array minus the real sum of the array
    def missing_number_2(self, nums):
        length = len(nums)
        sums = (length * (length + 1)) // 2
        return sums - sum(nums)

    # brute force naive answer. start at i = 0, check to see if it is present in array. if not return it.
    # time complexity O(N^2) because it can go from 0 -> N, and it has to check whole array? maybe we can hash it for O(N)?
    # Space: O(1) if you don't hash, O(N) if you do hash table.
    def missing_number_3(self, nums):
        n = len(nums)
        dic = {}
        i = 0
        for x in range(n):
            dic[nums[x]] = 1
        print(dic)
        while(True):
            if i in dic:
                i += 1
                continue
            else:
                return i



if __name__ == '__main__':
    input = [1]
    print(Solution.missing_number_3(0, input))