# initial thoughts: in a gramatically correct sentence,
# the number of words will be (number of spaces + 1)


def get_num_words(string):
    num_words = 0
    for x in string:
        if x == ' ':
            num_words += 1
    return num_words + 1


def get_num_words_split(string):
    return len(string.split(' '))


def get_num_words_count(input_string):
    return input_string.count(' ') + 1


if __name__ == '__main__':
    # 5 words, 4 spaces
    string = 'This is my test sentence'
    print(get_num_words_count(string))
