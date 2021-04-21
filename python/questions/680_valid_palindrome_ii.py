# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
#
# Input: "aba"
# Output: True
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
# Note:
#
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution(object):

    # My notes: so I was able to come up with the correct methodology on how to go about the problem
    # but I wasn't able to see that I could have used a recursive function, but I had all the other ideas correct
    # I need to work on being able to recognize recursive stuff, which usually involves shrinking the size of a input.

    # start with pointers at the beginning and end of the string and work our way towards the middle.
    # if the two pointers are not matching:
    #   if flag del 1 is already true, we've exceeded the delete count: return false
    #   if the left pointer's next == right's current OR right pointer's next == left's current, it's possible we can delete one. flag del 1
    #   continue with recursively going
    # if they are matching, increment and decrement pointers

    # Time: O(N) because it scales with the length of the input
    # Space: O(1) because our memory does not scale with the length of the input
    def valid_palindrome(self, s):
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s, left, right-1, True) or verify(s, left+1, right, True)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1, False)

print(Solution.valid_palindrome(0, 'abca'))
