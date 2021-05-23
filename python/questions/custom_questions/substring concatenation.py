# Find compound words that are in a list

# example_list = ['rockstar', 'rock', 'star', 'rocks', 'tar', 'star', 'rockstars', 'super', 'highway', 'high', 'way', 'superhighway']
#
# Identify all combinations where one word is a composite of two or more words from the same list and print or return them
#
# Example:
#
# rockstar -> rock + star
# superhighway -> super + highway
# superhighway -> super + high + way
#
# if returning, output would be a list of lists
#
# [['rock', 'star'], ['super', 'highway']]


# Brute force? Put all substrings of word into a dict. compare that dict to our example list
# example for rockstar, our dict would contain all of these:
# size of dict = n!, n = length of string
# r, ro, roc, rock, rocks, rockst, rocksta, rockstar
# o, oc, ock, ocks, ockst, ocksta, ockstar,
# c, ck, cks, ckst, cksta, ckstar
# k...
# s, st, sta, star
# t, ta, tar
# a...
# r

# for all words in example list, directly retrieve those in dictionary O(N).

def composite_list(word, example_list):
    string_combo_dict = {}
    string_combo = ''
    for x in range(len(word) + 1):
        for y in range(x, len(word) + 1):
            string_combo = word[x:y]
            string_combo_dict[string_combo] = 1
            string_combo = ''
    # for elem in string_combo_dict:
    #     print(elem)

    return_list = []
    for word in example_list:
        # print(word)
        if word in string_combo_dict:
            print(word)
            return_list.append(string_combo_dict[word])

    return return_list


def composite_list2(word, example_list):
    current_word = word
    for elem in example_list:
        if elem in current_word:
            print(elem)
            current_word = current_word.replace(elem, '')
            print(current_word)


if __name__ == '__main__':
    example_list = ['rockstar', 'rock', 'star', 'rocks', 'tar', 'star', 'rockstars', 'super', 'highway', 'high', 'way',
                    'superhighway']
    # print(composite_list('rockstar', example_list))
    list_of_words_input = ['rockstar','superhighway']
    print(composite_list2('rockstar', example_list))
