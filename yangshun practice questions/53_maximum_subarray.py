# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution(object):

    # Time Complexity O(N), Space O(1)
    # we set the first value to be our current max and we check if the next element would increase that max value.
    # if it does, then we add it and that sum is our new max current, and then we check to see if it is higher than max sum, and keeps whichever is higher.
    # we continue this process for each element in the array, because we only know if subsequent numbers will increase or decrease our current max.
    def maximum_subarray(self, nums):
        max_sum = nums[0]
        max_current = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_sum = max(max_sum, max_current)
        return max_sum


if __name__ == '__main__':
    input = [-2,1,-3,4,-1,2,1,-5,4]
    ret = Solution.maximum_subarray(0, input)
    print(ret)