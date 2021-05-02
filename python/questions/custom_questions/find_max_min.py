class Test():

    def find_max_min(array):
        min = array[0]
        max = array[0]
        for x in range(1, len(array)):
            if array[x] > max:
                max = array[x]
            if array[x] < min:
                min = array[x]
        return [min, max]

    def find_max_min_easy(array):
        return [min(array), max(array)]


if __name__ == '__main__':
    input = [4, 7, 109, 34, 86, -34, 12, 4, 8, 94]
    print(Test.find_max_min(input))
    print(Test.find_max_min_easy(input))
