# Delete reoccuring characters from string

class Test():

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
