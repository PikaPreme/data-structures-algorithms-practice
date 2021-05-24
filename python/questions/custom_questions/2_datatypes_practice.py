# datatypes practice


if __name__ == '__main__':

    # Tuples specifically use parenthesis
    # tuples is a collection which is ordered and unchangeable. Allows duplicate members. read only collections

    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    my_tuple2 = ('s', 'u', 'p', 'r', 'e', 'm', 'e',)
    print(my_tuple2)
    print(type(my_tuple))
    for x in range(0, len(my_tuple)):
        print(my_tuple[x])
    for x in my_tuple2:
        print(x)

    # sets use curly brackets
    # sets is a collection which is unordered and unindexed. No duplicate members.

    my_set = {10, 20, 30, 40, 50}
