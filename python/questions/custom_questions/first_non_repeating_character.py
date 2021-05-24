
# initial impressions
# iterate through string
#   # add characters to a dictionary where the values are the quantity of each letter
#   if letter is not in dictionary, add it to dictionary, quantity = 1
#   if letter is     in dictionary, increment quantity
# since dictionaries are ordered in insertion, return back the first letter in the dictionary that has a value of 1


def first_non_repeating_character(input_string):
    seen_letters = {}
    for character in input_string:
        if character in seen_letters:
            seen_letters[character] += 1
        else:
            seen_letters[character] = 1
    print(seen_letters)

    for element in seen_letters:
        if seen_letters[element] == 1:
            return element
    return '_'


if __name__ == '__main__':
    input = 'abcdefghijkl'
    print(first_non_repeating_character(input))