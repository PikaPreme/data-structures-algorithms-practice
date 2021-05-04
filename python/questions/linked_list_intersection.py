'''
notes



    v
[7, 1, 5, 6, 9, 11]
                 ^

               v
[100, 3, 6, 9, 11]


'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    # Traverse through linked list, fill list with memory values of nodes. see which one appears in both first
    # Time: O(N) + O(N) + O(N) = O(N)
    # space: O(2N) = O(N)

# time exceeds
def find_intersection(headA, headB):
    list1 = []
    A, B = headA, headB
    while A:
        list1.append(A)
        A = A.next

    while B:
        if B in list1:
            return B
        B = B.next
    return None


#
def getIntersectionNode(self, headA, headB):

    hash_table_A = {}
    while headA != None:
        hash_table_A[headA] = headA.next
        headA = headA.next
    while headB != None:
        if headB in hash_table_A:
            return headB
        headB = headB.next
    return None


if __name__ == '__main__':
    node1 = Node(7)
    node2 = Node(1)
    node3 = Node(5)
    node4 = Node(6)
    node5 = Node(9)
    node6 = Node(11)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    node100 = Node(100)
    node101 = Node(3)
    node100.next = node101
    node101.next = node4

    # print(node101.next == node4)
    print(find_intersection(node1, node100) == node4)
