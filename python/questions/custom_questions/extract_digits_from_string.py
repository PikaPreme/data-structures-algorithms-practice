class Test:

    # Time: O(N) where N = length of string
    # Space: O(N) Length of string. I believe b/c strings are immutable in python, so a new string is being made
    def extract_digits(string):
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for character in string:
            if character in digits:  # or character.isdigit()
                string = string.replace(character, '')
        return string

    def reduce_whitespace(self):
        data = 'Hello         I          Am            Columns            Commpany Name'
        for x in range(10):
            data = data.replace('   ', '  ')
        # print(data)
        data = data.split('  ')
        print(data)


if __name__ == '__main__':
    # print(Test.extract_digits('5iuk542g45g2g') == 'iukggg')
    # print(Test.extract_digits('123453') == '')
    # print(Test.extract_digits('gadfgsdrg') == 'gadfgsdrg')
    # print(Test.extract_digits('') == '')
    # print(Test.extract_digits('!@#$%^&*()') == '!@#$%^&*()')
    print(Test.reduce_whitespace(0))
