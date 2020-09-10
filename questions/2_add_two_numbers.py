# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#

# Thoughts: Even though the linked lists are stored in reverse order, it might be easier to keep it like that.
# They are currently stored in head = least significant bit, which might make it easier to do addition operations.
# Start at the heads, add them plus a carry bit, if the sum is greater than 10, we do modulo division to get the remainder and the remainder gets a carry bit = 1, append the linked list result with the remainder
# if the sum is lower than 10, we can just append it to the list and the carry is 0.
# continue until we reach null (assuming both length of list are same)
# if we have a carry & one list is null, just add carry and current list.
# if we have no carry, and one list is null, just point the result to the current node which will just append the rest of the list

#    2177
# 7777777

# ----------
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def add_two_numbers(self, l1, l2):
        carry = 0
        dummy = result = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            result.next = ListNode(carry % 10)
            carry //= 10                         # floor division. rounds down to nearest whole number
                                                 # basically if carry >= 10, it will be 1, else if carry < 10, it will be 0
            result = result.next
        return dummy.next


