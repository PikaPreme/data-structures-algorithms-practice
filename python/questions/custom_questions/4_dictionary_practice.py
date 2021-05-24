def basic_dict_functions():
    # dictionary, uses key value pairs
    # dict is a collection which is ordered* and changeable. No duplicate members. * as of python 3.6, they are insertion ordered

    my_dict = {'Judgment Dragon': 'Light', 'Dark Armed Dragon': 'Dark', 'Stardust Dragon': 'Wind'}
    # print(my_dict)
    for key in my_dict:
        print('{}: {}'.format(key, my_dict.get(key)))  # these are the keys, values
        # print()  # these are the values

    for key, val in my_dict.items():
        print('{}: {}'.format(key, val))

    new_card = 'Trishula'
    new_card_attr = 'Water'
    my_dict[new_card] = new_card_attr
    print(my_dict)


if __name__ == '__main__':
    basic_dict_functions()
