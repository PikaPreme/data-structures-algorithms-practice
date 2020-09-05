# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


# Brute force method: check all substrings and verify if it's a palindrome. Checking all substrings would be O(N^2) and verify palindrome would be O(N)
# so total would be O(N^3).
# O(N^2) method would be starting from the middle and expand from the middle and verify that characters on left and right side are matching.


class Solution(object):
    def longestPalindrome(s):
        result = ""
        for i in range(len(s)):
            odd = palindrome_at(s, i, i)
            even = palindrome_at(s, i, i + 1)

            result = max(result, odd, even, key=len)
        return result


# starting at l,r expand outwards to find the biggest palindrome
def palindrome_at(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


# print(Solution.longestPalindrome("babad"))
# print(Solution.longestPalindrome("cbbd"))
print(Solution.longestPalindrome("dammitimmadxyzxyzxyz"))

