# Find elements that exist in both lists
# Time: O(N) = N length a + M length b + L length dict
# Space: O(N) = N length of dict + M length of list
def find_elements_in_both_list():
    dict = {}
    list = []
    a = [1, 2, 3, 2, 3, 4, 3, 4, 5, 6]
    b = [7, 2, 10, 2, 7, 4, 9, 4, 9, 8]

    # put all elements into a dictionary. set their values to 1
    for x in range(0, len(a)):
        if a[x] not in dict:
            dict[a[x]] = 1

    # if the element in b exists in the dictionary, set that value to 2
    # this means it exists in both lists
    for y in range(0, len(b)):
        if b[y] in dict:
            dict[b[y]] = 2
    print(dict)

    # find all elements in the dict with a value of 2
    for z in dict:
        if (dict.get(z)) == 2:
            list.append(z)
    print(list)
    return


def add_elements_of_both_lists():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = []  # [5,7,9]
    for x in range(0, len(a)):
        c.append((a[x] + b[x]))
    return


def insert_list():
    test_list = [1, 3, 5, 7, 9]
    test_list.insert(1, 2)  # insert -> (index, object)
    print(test_list)  # [1, 2, 3, 5, 7, 9]


def two_dimension_list_practice():
    # create a 2D list and iterate through it
    deck_list = []
    monsters = ['BLS', 'Tour Guide', 'Maxx C', 'Caius']
    magics = ['Book of Moon', 'Monster Reborn', 'Scapegoat']
    traps = ['Solemn Warning', 'Trap Dustshoot']
    extra = ['Stardust Dragon', 'Black Rose Dragon', 'Formula Synchron']
    deck_list.append(monsters)
    deck_list.append(magics)
    deck_list.append(traps)
    deck_list.append(extra)

    # can go through list by using list[x][y]
    print(deck_list[3][0])  # Stardust Dragon

    print(deck_list)
    # deck_list = [['BLS', 'Tour Guide', 'Maxx C', 'Caius'],
    # ['Book of Moon', 'Monster Reborn', 'Scapegoat'],
    # ['Solemn Warning', 'Trap Dustshoot'],
    # ['Stardust Dragon', 'Black Rose Dragon', 'Formula Synchron']]

    # print elements in this 2D list by index
    # for x in range(len(deck_list)):
    #     for y in range(len(deck_list[x])):
    #         print(deck_list[x][y], end=', ')
    #     print()

    # print elements in this 2D list by element
    # for row in deck_list:
    #     for element in row:
    #         print(element, end=', ')
    #     print()


def basic_list_functions(test_list):
    # list.remove() - removes first occurrance from list
    test_list.remove(8)
    print(test_list)

    # list.pop() - removes element by index, returns removed element
    popped_number = test_list.pop(3)
    print(popped_number)

    # list.append() - adds element to end of the list
    test_list.append(420)
    print(test_list)

    # extend() - adds elements from iterable to the end of the list
    test_list.extend([69, 100, 169])
    print(test_list)

    # directly modifying an element in list
    test_list[0] = 6969
    print(test_list)


def enumerate_list_practice():
    sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # we can keep a counter, and reference each element directly from list
    for x, element in enumerate(sample_list):
        print('{} : {}'.format(x, element))

    # if we need to start at a specific index, use start= parameter
    for x, element in enumerate(sample_list, start=100):
        print('{} : {}'.format(x, element))


def basic_list_functions2():
    my_list = [10, 20, 30, 40, 50]
    print(my_list)
    print(type(my_list))

    # iterate through list using pointer
    for x in range(0, len(my_list)):
        print(my_list[x])

    # iterate through elements in list directly
    for x in my_list:
        print(x)


if __name__ == '__main__':
    # Lists use square brackets
    # list is a collection which is ordered and changeable. Allows duplicate members.
    # -indexed, from [0], [1], etc
    # similar to array in java
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # basic_list_functions(test_list)

    # two_dimension_list_practice()
    # insert_list()

    enumerate_list_practice()
