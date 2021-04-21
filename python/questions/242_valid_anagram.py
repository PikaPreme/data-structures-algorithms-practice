# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution(object):

    # naive brute force solution: add all the letters to a dictionary and increment values in multiple of same letters
    # compare the two dictionaries at the end to see if they match
    # Time complexity O(2N) -> O(N) because we go through each strings once
    # Space complexity O(2N) -> O(N) because we need a dictionary for both strings
    def is_anagram_1(self, s, t):
        dict1 = {}
        dict2 = {}
        for letter_s in s:
            if letter_s not in dict1:
                dict1[letter_s] = 1
            else:
                dict1[letter_s] += 1
        for letter_t in t:
            if letter_t not in dict2:
                dict2[letter_t] = 1
            else:
                dict2[letter_t] += 1
        if dict1 == dict2:
            return True
        else:
            return False

    # same as solution 1 but is cleaner code. not sure what the dict.get() does
    def is_anagram_1a(self, s, t):
        dict1 = {}
        dict2 = {}
        if len(s) != len(t):  # if the lengths don't match they can't be anagrams
            return False
        for letter in s:
            dict1[letter] = dict1.get(letter, 0) + 1
        for letter in t:
            dict2[letter] = dict2.get(letter, 0) + 1
        return dict1 == dict2


    def is_anagram_3(self, s, t):
        return sorted(s) == sorted(t)


    # very clever method, add all letters into a collection, then remove corresponding letters from collection.
    # if the collection is 0 at the end, then it's a match.
    def is_anagram_4(self, s, t):
        print('test')



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    ret = Solution.is_anagram_1(0,s,t)
    print(ret)
