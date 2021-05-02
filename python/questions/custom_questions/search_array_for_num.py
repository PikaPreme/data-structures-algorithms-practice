# search array for a number

class Test:

    def find_number(array, target):
        if not array or target not in array:
            return None
        for x in range(0, len(array)):
            if array[x] == target:
                return x

    def find_number_by_index(array, target):
        if not array or target not in array:
            return None
        return array.index(target)


if __name__ == '__main__':
    input = [1, 3, 5, 7, 9, 15, 32, 54]
    target = 1
    print(Test.find_number(input, target))
    print(Test.find_number_by_index(input, target))
