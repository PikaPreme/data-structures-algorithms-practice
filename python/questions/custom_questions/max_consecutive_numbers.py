# find max sequence of consecutive numbers
# [5,2,99,3,4,1,100]
# return 5 because {1,2,3,4,5} is greater than {99,10}


# start with a number. check if number-1 and number+1 are in input array. if that exists, we increment the count and keep searching x+1, x-1.

# keep track of visited numbers to save time

# start with first number
# put number in in visited dict
# check if number+1 in array
#    if yes, increment cur_seq count, put number+1 in visited, increment number
#    if no, that sequence ends
# check if number-1 in array
#    if yes, increment cur_seq count, put number-1 in visited, decrement number
#    if no, that sequence ends
# compare max_seq to cur_seq

# Time: O(N) because we will visit each element at least once.
# Space: O(N) because we store visited numbers in list = length of list
def find_consecutive(input_array):
    visited = []
    max_seq = 0

    for num in input_array:
        current_seq = 1
        if num in visited:
            print('already visited:{}'.format(num))
            pass
        else:
            print('currently checking:{}'.format(num))
            visited.append(num)
            x = num
            y = num
            while x + 1 in input_array:
                print('currently checking:{}'.format(x + 1))
                current_seq += 1
                visited.append(x + 1)
                x = x + 1
            while y - 1 in input_array:
                print('currently checking:{}'.format(y - 1))
                current_seq += 1
                visited.append(y - 1)
                y = y - 1
            if current_seq > max_seq:
                print('new max:{}'.format(current_seq))
                max_seq = current_seq
    return max_seq


if __name__ == '__main__':
    input = [5, 2, 99, 3, 4, 1, 100, 6, 98, 7, 5, 3]
    print(find_consecutive(input) == 7)
