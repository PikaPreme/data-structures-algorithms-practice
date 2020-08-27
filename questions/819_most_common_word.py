# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
#
#
#
# Example:
#
# Input:
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
#
#
#
# Note:
#
# 1 <= paragraph.length <= 1000.
# 0 <= banned.length <= 100.
# 1 <= banned[i].length <= 10.
# The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
# paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
# There are no hyphens or hyphenated words.
# Words only consist of letters, never apostrophes or other punctuation symbols.
#


class Solution(object):

    # Naive solution: go through each word in the paragraph, clean it from punctuation and capitalization,
    #   then check if in banned word(s), if it's not banned:
    #       add it to a hash map dictionary
    #       if it does exist, increment that value by 1, if it doesn't exist, add it and set the value to 1
    # return the max (dict, key=dict.get
    # Time: going thru paragraph and adding to hash table: O(N) depends on size of paragraph.
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        dict = {}
        banned = set(banned)

        for c in "!?',;:.":
            paragraph = paragraph.replace(c,' ')          # replaces all the punctuation with space
        paragraph = paragraph.lower().split()             # converts the paragraph to all lower case, then turns it into a list where each word is chosen by spaces.

        for word in paragraph:
            if word not in banned:
                if word in dict:                  # if the word exists in the dictionary
                    dict[word] += 1
                else:                           # if the word does not exist in the dictionary
                    dict[word] = 1

        return max(dict, key=dict.get)          # returns the key with the max value in dict. memorize this


