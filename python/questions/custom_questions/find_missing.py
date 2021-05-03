# finding missing element from 2 arrays
# [4,12,9,5,6]
# [4,9,12,6]
# return 5


# Time Complexity O(N * 2)
# Space Complexity O(1)
def find_missing(input1, input2):
    for x in input1:
        if x not in input2:
            return x
    for y in input2:
        if y not in input1:
            return y
    return None


# Time O(N).
# Converting to set is Linear time
# Taking difference of the 2 set, constant operation

# Space Complexity: Making an missing_items O(N)
# Space
def find_missing_set(input1, input2):
    missing_items = set(input1) - set(input2)
    return list(missing_items)[0]


# Add up sum of lists, take difference.
# Two sums, then a subtraction
def find_missing_by_sum(input1, input2):
    sum1 = sum(input1)
    print(sum1)
    sum2 = sum(input2)
    print(sum2)
    return abs(sum1 - sum2)


if __name__ == '__main__':
    # print(find_missing([4, 12, 9, 5, 6], [4, 9, 12, 6]) == 5)
    # print(find_missing([4, 9, 12, 6], [4, 12, 9, 5, 6]) == 5)
    # print(find_missing([4, 12, 9, 5, 6], [4, 9, 12, 5, 6]) == None)
    # print(find_missing([], []) == None)
    print(find_missing_by_sum([4, 12, 9, 5, 6], [4, 9, 12, 6]) == 5)
