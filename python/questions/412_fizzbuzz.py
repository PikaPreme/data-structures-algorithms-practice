# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


class Solution(object):

    # Naive solution. Iterate through n, check if its a multiple of 3 and multiple of 5, fizzbuzz, elif multiple of 3, elif multiple of 5
    # Time O(N)
    # Space O(1)
    def fizzBuzz(self, n):
        ret = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                print('FizzBuzz')
                # ret.append('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
                # ret.append('Fizz')
            elif i % 5 == 0:
                print('Buzz')
                # ret.append('Buzz')
            else:
                print(i)
                # ret.append(str(i))
        # return ret


print(Solution.fizzBuzz(0, 15))
