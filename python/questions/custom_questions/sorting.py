# Sort the elements in a list

class Sorting:

    # time: NLOGN
    # SPACE: O(N) - input shrinks, return grows
    # while the input array still has elements O(LOGN)
    #   iterate through input array, find smallest element O(N)
    #   Append smallest element to return list, remove element from input array.
    def sort_func_ltg(self, input):
        new_list = []
        while (input):
            min = input[0]
            for x in range(0, len(input)):
                if input[x] < min:
                    min = input[x]
            new_list.append(min)
            input.remove(min)
        return new_list

    def sort_func_gtl(self, input):
        new_list = []

        while (input):
            maximum = input[0]
            for x in range(0, len(input)):
                if input[x] > maximum:
                    maximum = input[x]
            new_list.append(maximum)
            input.remove(maximum)
        return new_list


if __name__ == '__main__':
    input = [5, 63, 234, 25, 84, 45, 72, 8, 2, 23, 45, 8, 8, 65, 8]

    print(Sorting.sort_func_ltg(0, input))
    print(Sorting.sort_func_gtl(0, input))

    # smallest to greatest
    input.sort()
    print(input)

    # reverse order
    input.sort(reverse=True)
    print(input)
