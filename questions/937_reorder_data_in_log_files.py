# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
#
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
#
#
# Example 1:
#
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
#
#
#
# Constraints:
#
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the identifier.
#

# Letter logs are before any digit logs


class Solution(object):

    # Naive brute force solution
    # go through the array of logs, determine type (letter-log or digit-log?). split by the space, check to see if digits, if not then its letters
    # maybe a divide and conquer method, where we put the letterlogs and digit logs into their own lists, and then sort the lists from there.
    # Then combine the lists after sorted. This would be trading space for time possibly.
    # for letter logs, prioritize the words, if it's a tie then use identifier.
    # Edges cases: [let1 art can, let1 art zero]? is this possible? compare can vs zero?
    # edge case: there is 'let' and 'dig' in the same log, so cannot use 'if xxx in method'

    # time complexity: splitting into two lists O(N), because we go through the array once.
    # Sorting each array O(log(n)) for each array ? so total O(nlogn)? because the size of the two smaller arrays would be each half
    # space complexity: O(N), the total space used would still be the size of the input.
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        dig_list = []
        let_list = []

        for element in logs:
            id = element.split(' ')
            if id[1].isdigit():
                dig_list.append(element)
            else:
                let_list.append(element)
        let_list.sort(key = lambda x: x.split(' ')[0])
        let_list.sort(key = lambda x: x.split(' ')[1:])
        let_list.extend(dig_list)
        return let_list








