# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
#
# Constraints:
#
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero

class Solution:

    # Time O(N) where n is max(len(a),len(b))
    # Space: O(N) where N is the max of the string lengths
    def addBinary(self, a: str, b: str) -> str:
        carry = 0                       # carry bit value
        result = ''

        a = list(a)                     # turn a and b into a stack
        b = list(b)

        while a or b or carry:          # while a or b are not empty, or if carry is 1. if a and b are empty and carry is 0, we are done
            if a:                       # if a is not empty, pop the least significant bit and add it to carry. (can be 0 or 1)
                carry += int(a.pop())
            if b:                       # if b is not empty, pop LSB and add it to carry (can be 0 or 1)
                carry += int(b.pop())

            result += str(carry %2)     # essentially append string of carry % 2, which is 0%2 = 0, 1%2=1, 2%2=0, 3%2=1
            carry //= 2                 # integer division, cuts off the decimal 0//2 = 0, 1//2 = 0, 2//2 = 1, 3//2 = 1

        return result[::-1]