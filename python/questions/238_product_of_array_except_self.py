# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution(object):

    # Naive brute force solution. For each element in the array, multiple together the numbers that are not the current element.
    # Time complexity O(N^2) because we iterate through the array once for each element in the array.
    # Space complexity O(1) because the output array does not count as extra space.
    def product_except_self(self, nums):
        products = []
        product = 1
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    product = product * nums[y]
            products.append(product)
            product = 1
        return products

    # Time complexity O(N).
    # No Division
    def product_except_self_2(self, nums):
        length_nums = len(nums)
        left_products = []
        right_products = []
        output = []

        for _ in range(length_nums):
            left_products.append(1)
            right_products.append(1)

        left_products[0] = 1
        right_products[length_nums - 1] = 1

        for x in range(1, length_nums):
            left_products[x] = left_products[x - 1] * nums[x - 1]
        print(left_products)

        for y in range(len(nums) - 2, -1, -1):
            right_products[y] = right_products[y + 1] * nums[y + 1]
        print(right_products)

        for z in range(0, len(nums)):
            output.append(left_products[z] * right_products[z])
        print(output)
        return output


#  v
# [1,2,3,4]


# [1,1,1,1]


if __name__ == '__main__':
    input = [1, 2, 3, 4]
    ret = Solution.product_except_self_2(0, input)
    print(ret == [24, 12, 8, 6])
