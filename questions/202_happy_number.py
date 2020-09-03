# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Questions: What if it's a single digit number? e.i 7, would we do 7^2 = 49, then 4^2 + 9^2 to continue the process?


# take the input number, split the digits individually, square them and sum them.
#   if the sum is equal to 1, then we can return True
#   if the sum is not 1, the sum is then the input for happy_number(n) again.
# question: when would we know when to return false?
# recursive solution is endless on some numbers

# Number Theory: if we reach a number we've already seen, then it is just an endless cycle.
# so we create a set and add numbers we've seen to the set, if we reach a number twice, then we return False
class Solution(object):
    def happyNumber(self, n):
        mem = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True


input = 19
print(Solution.happyNumber(0,19))
