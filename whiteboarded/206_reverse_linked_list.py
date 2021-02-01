# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    # start at the head, essentially flip the direction of next to previous and then increment through list
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        prev_node = None

        while curr_node:  # while the current node is not null
            next = curr_node.next  # we keep track of the next node so we can iterate at the end
            curr_node.next = prev_node  # point the direction of the node to the previous node (to reverse the direction)
            prev_node = curr_node  # set the prev node to current node (increments the head of new list)
            curr_node = next  # move onto the next node
        return prev_node  # previous is the head of the reversed linked list

    def reverse_list_recursive(self, head, prev=None):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverseList(next, head)
