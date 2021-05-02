# print 1
# 12
# 123
# 1234
# 12345


class Test():

    def print_pyramid(self, input):
        for x in range(1, input + 1):
            for y in range(1, x + 1):
                print(y, end='')
            print('\n', end='')

    def print_pyramid_string(self, input):
        string = ''
        for x in range(1, input + 1):
            string = string + str(x)
            print(string)


if __name__ == '__main__':
    Test.print_pyramid_string(0, 5)
