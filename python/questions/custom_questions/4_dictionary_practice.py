def basic_dict_functions():
    # dictionary, uses key value pairs
    # dict is a collection which is ordered* and changeable. No duplicate members. * as of python 3.6, they are insertion ordered

    my_dict = {'Judgment Dragon': 'Light', 'Dark Armed Dragon': 'Dark', 'Stardust Dragon': 'Wind'}
    # print(my_dict)
    for key in my_dict:
        print(key)  # these are the keys
        print(my_dict.get(key))  # these are the values

    for key, val in my_dict.items():
        print(key)
        print(val)


if __name__ == '__main__':
    basic_dict_functions()
