# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
#
# Example 2:
#
# Input: "()[]{}"
# Output: true
#
# Example 3:
#
# Input: "(]"
# Output: false
#
# Example 4:
#
# Input: "([)]"
# Output: false
#
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # must close the most recent bracket before closing older brackets
        # each bracket must have respective partner (e.g one of each)
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:  # for every char in input string
            print(char)
            if char in dict:  # if the char exists in the dictionary
                print('char: {} exists in dictionary'.format(char))
                stack.append(dict[char])  # append the closing pair to the stack
                print('stack: {}'.format(stack))
            elif not stack or stack.pop() != char:
                # if not stack or we pop the stack and make sure its equal to char.
                # make sure the proper pair closes, if it doesn't then it's false
                print('not stack {}. or stack.pop != char: {}'.format(stack, char))
                return False
            print('current stack: {}'.format(stack))
        return len(stack) == 0

    def is_valid_nc(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # must close the most recent bracket before closing older brackets
        # each bracket must have respective partner (e.g one of each)
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in dict:
                stack.append(dict[char])
            elif not stack or stack.pop() != char:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    # input = "()"
    input = "()[]{}"
    # input = "(]"
    # input = "([)]"
    # input = "{[]}"
    ret = Solution.is_valid(0, input)
    print(ret)
