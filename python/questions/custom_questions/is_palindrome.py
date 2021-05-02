class Test(object):

    def is_palindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = 'dammitimmad'
    print(Test.is_palindrome(s))
