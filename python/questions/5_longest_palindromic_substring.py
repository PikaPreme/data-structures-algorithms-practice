# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#             |
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
# O(N log n) method would be starting from the middle and expand from the middle and verify that characters on left and right side are matching.


class Solution(object):
    def longestPalindrome(input_string):
        longest_pali = ""
        for i in range(len(input_string)):
            odd = palindrome_at(input_string, i, i)
            even = palindrome_at(input_string, i, i + 1)
            # longest_pali = max(longest_pali, odd, even, key=len)

            # alternative to longest_pali 1 liner
            # compare our current longest palindrome, against the two palindromes we just made (odd, even)
            # keep whichever is the longest palindrome (by length)
            if len(odd) > len(longest_pali) or len(even) > len(longest_pali):
                if len(odd) > len(even):
                    longest_pali = odd
                else:
                    longest_pali = even

        return longest_pali


# starting at l,r expand outwards to find the biggest palindrome
def palindrome_at(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1: r]

    # even numbered string
    #   v
    # abccba
    #    ^
    #
    # odd numbered string
    #           v
    # d a m m i t i m m a d
    #           ^


if __name__ == '__main__':
    # print(Solution.longestPalindrome("babad"))
    # print(Solution.longestPalindrome("cbbd"))
    print(Solution.longestPalindrome("dammitimmadxyzxratstaryzxyz"))
