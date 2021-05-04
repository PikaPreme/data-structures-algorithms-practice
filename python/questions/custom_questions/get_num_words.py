class Test():

    def get_num_words(string):
        num_words = 0
        for x in string:
            if x == ' ':
                num_words += 1
        return num_words + 1

    def get_num_words_split(string):
        return len(string.split(' '))


if __name__ == '__main__':
    string = 'I am having a very nice day.'
    print(Test.get_num_words_split(string))