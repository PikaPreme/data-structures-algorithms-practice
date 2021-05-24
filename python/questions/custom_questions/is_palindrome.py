class Test(object):

    # Pythonic way, use [::-1] to reverse the string, check if that is equal to original string
    # Time: O(N) - not sure how reverse notation works under the hood, but most likely O(N)
    # Space: O(1) - we're not saving anything in memory, but most likely memory will be used temporarily to reverse string
    def is_palindrome(s):
        if s == s[::-1]:
            return True
        else:
            return False

    # odd length word: middle letter can be singular, everything else must mirror
    # even length word: first half must mirror second half
    # example, length of word = 11, letters 1-5 must mirror 7-11, 6th letter is single
    # example, length of word = 10, letters 1-5 must mirror 6-10

    # for programming, the length is len-1 (because of 0 index)
    # half way point can be made for both even and odd, by using floor divison //
    # 10 // 2 = 5        11 // 2 = 5

    # one pointer at start, one pointer at end
    # move them towards the center until they meet each other. range = half
    # continuously check if they are equal

    # Time: O(N)
    # Space: O(1) not storing
    # edge cases: empty string
    def is_palindrome2(str):
        if not str:
            return False
        length = len(str) - 1
        half = length // 2
        for x in range(0, half):
            if str[x] == str[length]:
                length -= 1
            else:
                return False
        return True

        #   v
        # abccba
        #    ^
        #           v
        # d a m m i t i m m a d
        #           ^


if __name__ == '__main__':
    s = 'dammitimmad'
    print(Test.is_palindrome2(s) == True)
    print(Test.is_palindrome2('abccba') == True)
    print(Test.is_palindrome2('') == False)
    print(Test.is_palindrome2('dammittimmad') == True)
    print(Test.is_palindrome2('dammittimmaad') == False)
    print(Test.is_palindrome2('neveroddoreven') == True)
