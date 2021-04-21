# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
#
# Example 2:
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # naive solution, take the linked list and append it to a list, see if that list is a palindrome
    # time complexity O(N), traverse through the linked list O(N), and verify palindrome is same backwards O(N). so O(2N) -> O(N)
    # Space complexity O(N) because we're using a list based on the length of the list
    def palindrome(self, head):
        # palindrome_list = []
        # while head:
        #     palindrome_list += head.val,
        #     head = head.next
        # return palindrome_list == palindrome_list[::-1]

        vals = []
        while head:
            vals += head.val,
            head = head.next
        return vals == vals[::-1]

input = [1,2]
print(Solution.palindrome(0, input))