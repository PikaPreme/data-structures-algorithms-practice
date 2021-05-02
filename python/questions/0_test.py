class Solution:

    def func(self, input, target):

        for x in range(0, len(input)):
            difference = target - input[x]
            if difference in input and x != input.index(difference):
                return [x, input.index(difference)]


    def func2(self, input, target):
        dict = {}
        for x in range(0, len(input)):
            difference = target - input[x]
            dict[difference] = x
            if input[x] in dict:
                return [dict[input[x]], x]





if __name__ == '__main__':
    input = [2,5,7,11]
    target = 13
    print(Solution.func(0, input, target))