# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class Solution(object):


    # Naive solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = sorted_list = ListNode(0)
        while( l1 and l2):                          # while the lists are not null
            if (l1.val < l2.val):                   # check for which value is smaller
                sorted_list.next = l1               # sorted list now points to the smaller value
                l1 = l1.next                        # move L1 onto the next value
                sorted_list = sorted_list.next      # move sorted onto next value
            elif l1.val >= l2.val:
                sorted_list.next = l2
                l2 = l2.next
                sorted_list = sorted_list.next

        sorted_list.next = l1 or l2             # once one of them reaches null, it attaches the remaining list to the end
        return head.next                        # (meaning the rest of the values are greater)
