# Write a SQL query to get the second highest salary from the Employee table.
#
# +----+--------+
# | Id | Salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
#
# For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.
#
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+

# I will do this in python



class Solution(object):

    # Naive solution: Find the highest number, remove it from the list. Then find the highest number.
    # This question can be made dynamically to find the Nth highest salary by looping to the Nth highest salary
    # edge cases, multiple people with equal highest salary, removing the highest wouldn't change the solution so we have to negate the increment
    def second_highest(self, nums):
        n = 1
        highest = max(nums)
        while x < n:
            nums.remove(max(nums))
            x = x + 1
            if max(nums) == highest:
                x = x - 1
        return max(nums)

    def nth_highest(self, nums, n):
        if len(nums) < 2:
            return None
        highest = max(nums)
        x = 1
        while x < n:
            nums.remove(max(nums))
            x = x + 1
            if max(nums) == highest:
                x = x - 1
        return max(nums)

    # Naive solution 2: sort the array, go to the second to last index as long as it's not equal to the highest


# input = [1,2,3,4,5,6,7,8,50,69]
# print(Solution.second_highest(0, input))

input = [1,69]
print(Solution.nth_highest(0, input, 2))  # 1 = higehst, 2 = second highest
