# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
#
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#
#
# Constraints:
#
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1.length == m + n
# nums2.length == n


class Solution(object):

    # Naive Easy Pythonic Solution: simply combine the two lists and sort them.
    # this is not the most optimal, because it doesn't take advantage that they're already sorted.
    # Time complexity: O( (n+m)log(n+m) )
    # Need to do nums1[:], not nums1 because it wants to modify nums1 in place, if we do nums1 = , python creates a new object named nums1
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])

    # Naive Easy python Solution #2:
    # fill up nums1 list from the last element to the sum of both elements, with the elements of nums2. Then sort
    def merge2(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return
        nums1[m:m + n] = nums2[:n]
        nums1.sort()

    # Algorithmic solution
    def merge3(self, nums1, m, nums2, n):
        index = len(nums1) - 1
        m -= 1
        n -= 1
        print('Start. Index: {}, m: {}, n: {}'.format(index, m, n))
        while n >= 0:
            print('while n = {} >= 0'.format(n))
            if m < 0 or nums1[m] < nums2[n]:
                print('if m = {} < 0 OR nums1[m] = {} < {} = nums2[n]'.format(m, nums1[m], nums2[n]))
                nums1[index] = nums2[n]
                n -= 1
            else:
                print('else')
                nums1[index] = nums1[m]
                m -= 1
            print(nums1)
            index -= 1


nums1 = [1, 2, 3, 5, 7, 9, 0, 0, 0, 0, 0, 0]
m = 6
nums2 = [2, 5, 6, 7, 8, 11]
n = 6
