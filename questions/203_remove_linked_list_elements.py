# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # Naive Method: Starting at the head, traverse through the linked list.
    # If the current node's value is the input value, make the previous point to the next node.
    # if current.val == val:
    #   previous.next = current.next

    # Keep track of next, current, and previous. In order to safely increment:
    # next = current.next
    # previous = current
    # current = next

    # Edge cases: head to be deleted. set a dummy, and refer to dummy.next as return (head)
    # if the real head has to be deleted, can we make dummy.next = current.next

    # Time: O(N) passes through the linked list once
    # Space: O(1) constant
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-5)
        dummy.next = head
        current = head
        previous = dummy

        while current != None:
            if current.val == val:
                previous.next = current.next
                current = current.next
            else:
                previous = current
                current = current.next
        return dummy.next
