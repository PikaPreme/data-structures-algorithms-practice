# Lists
# -ordered, changeable, allow duplicates
# -indexed, from [0], [1], etc


if __name__ == '__main__':
    # a = [1,2,3]
    # b = [4,5,6]
    # c = []
    #
    # for x in range(0,len(a)):
    #     c.append((a[x] + b[x]))
    #
    # print(c)

    dict = {}
    list = []
    a = [1,2,3,2,3,4,3,4,5,6]
    b = [7,2,10,2,7,4,9,4,9,8]
    for x in range(0, len(a)):
        if a[x] not in dict:
            dict[a[x]] = 1
    for y in range(0, len(b)):
        if b[y] in dict:
            dict[b[y]] = 2
    print(dict)
    for z in dict:
        if(dict.get(z)) == 2:
            list.append(z)
    print(list)