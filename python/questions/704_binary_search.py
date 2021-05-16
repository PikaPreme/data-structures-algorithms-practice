class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1

        # target = 8
        #  v
        # [1,2,3,4,5,6,7,8,9,10]
        #        ^

    def search2(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
