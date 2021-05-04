'''

 v
[2,8,3,11]


Given target 11 -> return [1,2]

If no valid pairs, return None
If not valid list, return None

Naive method: Brute Force - check all combinations if they add to target
Time: O(N^2) because we iterate through the length of the input for both indexes
Space: O(1) - not using any memory to store values


method 2: iterate through list
check for the difference (target - current number)
if exists in list. if it does: return that number
Time: O(N) - iterate through list once
Space: O(1) - not using any memory to store values


method 3: hash method
if the number is not apart of the dictionary:
    load up the difference into dict
    load the dict { key: difference, value: index }
if the number IS in dict:
    return valid pair: [dict), current_index]

TIME: O(N) - iterate through list once. faster in runtime due to hash mapping O(1)
Space: O(N) - fill up a dictionary to the size of list

'''


class Solution:
    # Time complexity O(N^2) because it loops through the list for each element
    # Space complexity O(1) because no values are being stored
    # We check every combination of x and y, and compare the sum of (x+y) to the target. If it's a match we return the indexes
    # Simplest way is to have a double for loop to check all pairs of x and y.
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
                if x < nums.index(diff):
                    return [x, nums.index(diff)]
                else:
                    return [nums.index(diff), x]

    # one hash pass solution,
    # Time Complexity O(N) - much faster in run time but still
    # Space complexity O(N)Trade off is that we have to save the diff value, trading space for time.
    def twoSum(self, nums, target):
        dic = {}
        # for i, num in enumerate(nums):
        for i in range(0, len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                diff = target - nums[i]
                dic[diff] = i


if __name__ == '__main__':
    # print(Solution.two_sum(0, [1,3,2,6,8], 5) == [1,2])
    # print(Solution.two_sum(0, [1,3,3,6,8], 6) == [1,2])
    # print(Solution.two_sum(0, [], 5) == None)
    # print(Solution.two_sum(0, [-5], 5) == None)
    # print(Solution.two_sum(0, [1,3,2,6,8], 20) == None)
    # print(Solution.two_sum(0, [1,3,2,6,8, -1], 0) == [0,5])
    # print(Solution.two_sum(0, [1,3,2,6,8, -1,-4], -5) == [5,6])
    # print(Solution.two_sum(0, [5,5], 10) == [0,1])

    print(Solution.twoSum(0, [1,3,2,6,8], 5) == [1,2])
    print(Solution.twoSum(0, [1,3,3,6,8], 6) == [1,2])
    print(Solution.twoSum(0, [], 5) == None)
    print(Solution.twoSum(0, [-5], 5) == None)
    print(Solution.twoSum(0, [1,3,2,6,8], 20) == None)
    print(Solution.twoSum(0, [1,3,2,6,8, -1], 0) == [0,5])
    print(Solution.twoSum(0, [1,3,2,6,8, -1,-4], -5) == [5,6])
    print(Solution.twoSum(0, [5,5], 10) == [0,1])

    # print(Solution.two_sum_naive(0, [1,3,2,6,8], 5) == [1,2])
    # print(Solution.two_sum_naive(0, [1,3,3,6,8], 6) == [1,2])
    # print(Solution.two_sum_naive(0, [], 5) == None)
    # print(Solution.two_sum_naive(0, [-5], 5) == None)
    # print(Solution.two_sum_naive(0, [1,3,2,6,8], 20) == None)
    # print(Solution.two_sum_naive(0, [1,3,2,6,8, -1], 0) == [0,5])
    # print(Solution.two_sum_naive(0, [1,3,2,6,8, -1,-4], -5) == [5,6])
    # print(Solution.two_sum_naive(0, [5,5], 10) == [0,1])
