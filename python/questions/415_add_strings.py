# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):

    # num1 and num2 are strings.
    # I could go through the strings revsered, multiply the weight by the digit and sum it all. (e.g. 350 = (0*1) + (5*10) + (3*100)
    # naive solution:
    # time: O(2N) => O(N) because we iterate through the size of each number once.
    # space: O(1) because the memory used does not scale with the input size.
    def add_string(self, num1, num2):
        numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        num1 = num1[::-1]
        num2 = num2[::-1]
        output = 0
        sigfig = 0
        for c in num1:
            output = output + (numDict.get(c) * 10**sigfig)
            sigfig += 1
        sigfig = 0
        for c in num2:
            output = output + (numDict.get(c) * 10**sigfig)
            sigfig += 1
        return str(output)

print(Solution.add_string(0, '135', '732'))