class Test(object):

    def is_palindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False

    def is_palindrome2(str):
        if not str:
            return False
        length = len(str) - 1
        half = length // 2
        index = 0
        for x in range(0, half):
            if str[x] == str[length]:
                length -= 1
            else:
                return False
        return True

        #   v
        # abccba
        #    ^
        #                 v
        # d a m m i       t     i m m a d
        #                 ^


if __name__ == '__main__':
    s = 'dammitimmad'
    print(Test.is_palindrome2(s) == True)
    print(Test.is_palindrome2('abccba') == True)
    print(Test.is_palindrome2('') == False)
    print(Test.is_palindrome2('dammittimmad') == True)
    print(Test.is_palindrome2('dammittimmaad') == False)
    print(Test.is_palindrome2('neveroddoreven') == True)
