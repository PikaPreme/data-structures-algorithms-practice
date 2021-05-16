# search array for a number


# Time: O(N), size of the array
# Space: O(1) no space used
def find_number(input_array, target):
    if not input_array or target not in input_array:
        return None
    for x in range(0, len(input_array)):
        if input_array[x] == target:
            return x


# Time: O(N)
def find_number_by_index(array, target):
    if not array or target not in array:
        return None
    return array.index(target)


if __name__ == '__main__':
    input = [1, 3, 5, 7, 9, 15, 32, 54]
    target = 32
    print(find_number(input, target) == 6)
    print(find_number_by_index(input, target) == 6)
