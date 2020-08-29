# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Note:
#
# All given inputs are in lowercase letters a-z.

# Fight, Fighting, Fighter

# Naive solution: Compare each letter in each word to each other, if they match then continue, and increment letter index
# if it manages to clear all the letters, that means the letter is common, so we can append it to the output.
# edge case: empty, just return output ''
# Time: O(N) for each word in array, and O(M) for length of the shortest word.
# Space: O(1) only using constant extra space (one output)

class Solution(object):
    def longest_common_prefix(self, strs):
        output = ''
        if not strs:
            return output
        minimum = min(len(word) for word in strs)
        for x in range(0,minimum):
            for y in range(1,len(strs)):
                if strs[y][x] != strs[0][x]:
                    return output
            output += strs[0][x]
        return output



