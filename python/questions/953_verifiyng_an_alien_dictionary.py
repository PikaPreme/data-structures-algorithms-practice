# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
#
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
#
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
#
#
#
# Constraints:
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
#

class Solution(object):

    # possibly create a hash map (dictionary) to map out the order and their respective values.
    # go through the list of words from 1 to n, and compare the first letters of the words against the word before it to make sure its lexiographically sorted
    # if the word prior has a letter value that is higher than the current word's letter, that would be a false statement.
    # similar words, increment through each letter until a different letter is found
    # edge cases: empty list, not lowercase letters. multiple of same word. similar wards but extended (apple vs app)
    def is_alien_sorted(self, words, order):
        order_dict = {}
        for x in range(0,len(order)):
            order_dict[order[x]] = x
        print(order_dict)

        for y in range(1,len(words)):
            word1 = words[y-1]
            word2 = words[y]

            if not words[y][0].islower():       # edge case: anything not lower case
                return False
            if len(word2) < len(word1):         # edge case: similar words but extended (app vs apple)
                if word1.startswith(word2):
                    return False

            for z in range(0,min(len(word2), len(word1))):        # go through each letter in each word
                if order_dict[word2[z]] < order_dict[word1[z]]: # if the next word's letter is less than the previous, false
                    return False
                elif order_dict[word2[z]] == order_dict[word1[z]]:  # if letters are equal, continue
                    continue
                else:
                    break
        return True








