# Given a word, you need to judge whether the usage of capitals in it is right or not.
#
# We define the usage of capitals in a word to be right when one of the following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
#
#
# Example 1:
#
# Input: "USA"
# Output: True
#
#
#
# Example 2:
#
# Input: "FlaG"
# Output: False
#
#
#
# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

class Solution(object):

    # Use flags to determine have been used. any incorrect cases will result in a false.
    # Go through each letter in word, if the first letter is capitalized we mark a flag.
    # If they're all capital it's okay, if any other capitals appear it's false.
    # if all lowercase (capitalized flag is false) then it's okay.
    # if we've seen 2 caps, flag two_caps
    # time O(N)
    # space O(1)
    def detect_capital(self, word):
        n = len(word)
        cap = False
        lower = False
        two_caps = False
        for x in range(0, n):
            if word[x].isupper():
                if lower:
                    return False
                if not cap:
                    cap = True
                else:
                    two_caps = True
            else:
                if (two_caps):
                    return False
                lower = True
        return True

    def detect_capital_2(self, word):
        return word.isupper() or word.islower() or word.istitle()

# USA
# Google
# leetcode
# FFf

if __name__ == '__main__':
    input1 = 'USA'
    input2 = 'Google'
    input3 = 'leetcode'

    input4 = 'FFFFFFFf'
    input5 = 'fFFFFFFF'
    input6 = 'FlaG'
    input7 = 'flaG'
    print(Solution.detect_capital(0, input1))
    print(Solution.detect_capital(0, input2))
    print(Solution.detect_capital(0, input3))
    print(Solution.detect_capital(0, input4))
    print(Solution.detect_capital(0, input5))
    print(Solution.detect_capital(0, input6))
    print(Solution.detect_capital(0, input7))
