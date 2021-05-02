class Test:

    def print_duplicates(input):
        input.sort()
        answer = []
        for x in range(0, len(input) - 1):
            if input[x] == input[x + 1]:
                answer.append(input[x])
        return answer

    def print_duplicates_no_sort(input):
        answer = []
        for num in input:
            if input.count(num) > 1:
                if num not in answer:
                    answer.append(num)
        return answer


if __name__ == '__main__':
    input = [1, 2, 3, 4, 4, 5, 5, 6, 1]
    print(Test.print_duplicates(input))
    print(Test.print_duplicates_no_sort(input))
