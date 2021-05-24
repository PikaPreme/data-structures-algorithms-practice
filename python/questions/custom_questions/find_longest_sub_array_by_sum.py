# find longest continuous subarrays
#
# brute force: look at all combinations and see if they add up to sum, record the length and keep that value.
# if the sum of current numbers, > target sum, we can break and go to next outter pointer
# if the length is longer than max length, we can update that result
# nested for loops, probably n^2

# sliding window approach, instead of sending right pointer back to the beginning,
# we can move our left pointer along, and subtract that
# subtract current left pointer, then increment left pointer


# start with 2 pointers at 0,
# if the sum < target, increment right pointer and add value to sum
# if the sum = target, record the two pointers, and their distance, compare it to current max pointers and distance. then increment and add
# if the sum > target, subtract left pointer from sum, increment left

#                                                      v
# arr = [1, 2, 3, 6, 3, 5, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
#                                                      ^
# sum = 15
# r=[1,8]

def find_longest_sub_array(input_list, target):
    left = 0
    right = 0
    distance = 0
    sum = input_list[0]
    out = []

    while right < (len(input_list) - 1) or left < (len(input_list) - 1):
        print('Current pointers: {} -> {} = Sum: {}'.format(left, right, sum))
        if sum < target:
            right += 1
            sum += input_list[right]
        elif sum > target:
            sum -= input_list[left]
            left += 1
        elif sum == target:
            print('target found: {}'.format(sum))
            if right - left > distance:
                distance = (right - left) + 1
                out = [left, right]
            right += 1
            sum += input_list[right]
    print('Current pointers: {} -> {} = Sum: {}'.format(left, right, sum))

    return out, distance


if __name__ == '__main__':
    #      0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  15 16                  22
    arr = [1, 2, 3, 6, 3, 5, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
    print(find_longest_sub_array(arr, 13))
