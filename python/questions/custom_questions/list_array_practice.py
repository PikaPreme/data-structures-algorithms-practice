# Find elements that exist in both lists
def find_elements_in_both_list():
    dict = {}
    list = []
    a = [1, 2, 3, 2, 3, 4, 3, 4, 5, 6]
    b = [7, 2, 10, 2, 7, 4, 9, 4, 9, 8]
    for x in range(0, len(a)):
        if a[x] not in dict:
            dict[a[x]] = 1
    for y in range(0, len(b)):
        if b[y] in dict:
            dict[b[y]] = 2
    print(dict)
    for z in dict:
        if (dict.get(z)) == 2:
            list.append(z)
    print(list)
    return


def add_elements_of_both_lists():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = []
    for x in range(0, len(a)):
        c.append((a[x] + b[x]))
    return


if __name__ == '__main__':
    # Lists
    # -ordered, changeable, allow duplicates
    # -indexed, from [0], [1], etc
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
