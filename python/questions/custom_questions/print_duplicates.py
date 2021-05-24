class Test:

    # not very good solution
    # Sorting the array, makes it very easy to check adjacent numbers for duplicates.
    # add any duplicated numbers to a dictionary.
    # Time: O(N log(n)) because we sorted it
    def print_duplicates(input):
        input.sort()
        answer = {}
        for x in range(0, len(input) - 1):
            if input[x] == input[x + 1]:
                answer[input[x]] = 1
        return answer.keys()

    # this method counts number of instances of number in the list
    # if > 1: add it to a list
    # Time: O(N)
    # Space: O(N)
    def print_duplicates_no_sort(input):
        answer = []
        for num in input:
            if input.count(num) > 1:
                if num not in answer:
                    answer.append(num)
        return answer

    # iterate through list:
    # add numbers to dict
    # if they are already in dict, mark them with 2
    # any number with 2 = duplicate.
    # return all numbers with 2
    # Time: O(N) - goes through all numbers in input list
    # Space: O(N) - space for duplicates, space for return list
    def print_duplicates_dict(input):
        duplicates = {}
        return_list = []
        for num in input:
            if num in duplicates:
                duplicates[num] = 2
            else:
                duplicates[num] = 1
        for item in duplicates:
            if duplicates[item] == 2:
                return_list.append(item)
        return return_list


if __name__ == '__main__':
    # input =
    print(Test.print_duplicates([34, 1, 2, 3, 34, 4, 4, 5, 5, 6, 1, 5, 4, 6, 1, 5, 5, 5]))
    print(Test.print_duplicates_no_sort([34, 1, 2, 3, 34, 4, 4, 5, 5, 6, 1, 5, 4, 6, 1]))
    print(Test.print_duplicates_dict([34, 1, 2, 3, 34, 4, 4, 5, 5, 6, 1, 5, 4, 6, 1]))
