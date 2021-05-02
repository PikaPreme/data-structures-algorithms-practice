class Test():

    def extract_digits(string):
        for character in string:
            if character.isdigit():
                string = string.replace(character, '')
        return string

print(Test.extract_digits('5iuk542g45g2g'))