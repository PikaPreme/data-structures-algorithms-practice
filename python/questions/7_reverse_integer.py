# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
#
# Example 2:
#
# Input: -123
# Output: -321
#
# Example 3:
#
# Input: 120
# Output: 21
#
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution(object):

    # naive brute force solution: take the absolute value of the number, convert it to a string then use [-1::] to reverse it
    # if the number was negative, return -rev, if number was positive, return rev
    # make sure the bit length is less than 32
    # Time: O(1)
    # Space: O(1)
    def reverse_integer(self, x):
        if x == 0:
            return 0
        rev = int(str(abs(x))[::-1])
        if rev.bit_length() < 32:
            if x > 0:
                return rev
            elif x < 0:
                return -rev
        else:
            return 0


if __name__ == '__main__':
    input = 123
    input2 = -123
    input3 = 120
    input4 = -120
    print(Solution.reverse_integer(0, input))
    print(Solution.reverse_integer(0, input2))
    print(Solution.reverse_integer(0, input3))
    print(Solution.reverse_integer(0, input4))
