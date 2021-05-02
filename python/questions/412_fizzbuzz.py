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


class Fizz():

    def fizz_buzz(self, input):
        for x in range(1, input + 1):
            if x % 3 == 0 and x % 5 == 0:
                print('fizzbuzz')
            elif x % 3 == 0:
                print('fizz')
            elif x % 5 == 0:
                print('buzz')
            else:
                print(x)

    def fizz_buzz_string(self, input):
        for x in range(1, input + 1):
            string = ''
            if x % 3 == 0:
                string += 'Fizz'
            if x % 5 == 0:
                string += 'Buzz'
            if x % 3 != 0 and x % 5 != 0:
                string = x
            print(string)

    def fizz_buzz_return_array(self, input):
        return_array = []
        for x in range(1, input + 1):
            if x % 3 == 0 and x % 5 == 0:
                return_array.append('FizzBuzz')
            elif x % 3 == 0:
                return_array.append('Fizz')
            elif x % 5 == 0:
                return_array.append('Buzz')
            else:
                return_array.append(x)
        return return_array


if __name__ == '__main__':
    Fizz.fizz_buzz_string(0, 15)
    Fizz.fizz_buzz(0, 15)
    print(Fizz.fizz_buzz_return_array(0, 15))
