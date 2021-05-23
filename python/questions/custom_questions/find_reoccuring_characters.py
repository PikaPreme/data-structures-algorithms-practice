# Delete reoccuring characters from string

class Test():

    # iterate through string
    #   if the letter is not in the set,
    #       add it to the set.
    #       modify string with letter
    # Time: o(N) - length of input string
    # Space: O(N) - length of input string
    def del_reoccuring_chars(input):
        seen_characters = set()
        out = ''
        for letter in input:
            if letter not in seen_characters:
                out = out + letter
                seen_characters.add(letter)
        return out

if __name__ == '__main__':
    print(Test.del_reoccuring_chars('dammitimmad'))
    print(Test.del_reoccuring_chars('abcdefghijklmnopqrstuvwxyzabc'))
    print(Test.del_reoccuring_chars('aaaaaaaaaaaaaaaaa'))


