# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.



class Solution(object):

    # Naive Solution: given the list of nums, I would traverse through the array, if the element is zero,
    # remove it from the list then append to list, since we add it to the end of the list, we need to decrease the length by 1
    # if it's a normal number we just continue, so i +=1
    def move_zeroes(self, nums):
        i = 0
        n = len(nums)
        # for x in range(0,len(nums)):
        while i < n:
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                n -= 1
            else:
                i += 1
        return nums

input = [1,0,0,0,0,1,0,3,12]
print(Solution.move_zeroes(0, input))