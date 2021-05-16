# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
# Example 1:
#
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
# Example 2:
#
# Input: s = "a"
# Output: 1
#
# Example 3:
#
# Input: s = "bb"
# Output: 2

# bbbaaaaa -> baaaaab,

# Initial impressions solution
# iterate through string and count all letters, keep tracking of the quantity. Lower case and upper case are seperate
# letters that have an even number quantity can be added to the palindrome, because they can be mirrored
# letters that have an odd number quantity can be added to palindrome, but must have 1 remaining.
# we can have a single letter in the middle for an odd numbered palindrome


def longest_palindrome(s):
    character_dict = {}
    for char in s:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] = character_dict[char] + 1
    print(character_dict)

    string_count = 0
    odd = 0

    for character in character_dict:
        if character_dict[character] % 2 == 0:
            string_count += character_dict[character]
        elif character_dict[character] % 2 == 1:
            odd = 1
            string_count += character_dict[character] - 1

    return string_count+odd


if __name__ == '__main__':
    print(longest_palindrome('bbbaaaaa'))
