if __name__ == '__main__':
    # 1
    x = 0
    x = x == x
    print(x)
    # out: True

    # 2
    list1 = [1, 2, 3]
    list2 = list1[-2:-1]
    list3 = list2[-1:-2]
    print(list2, list3)
    # out: [2] []

    # 3
    oldList = [1, 2, 3]
    for i in range(len(oldList)):
        oldList.insert(i, 0)
    print(oldList)
    # out: [0, 0, 0, 1, 2, 3]

    # 4
    my_list = [1, 2, 3, 4, 5]
    my_list[1], my_list[2] = my_list[2], my_list[1]
    print(my_list)
    # out: [1, 3, 2, 4, 5]

    # 5
    alphabets = ['a', 'b', 'c']
    del alphabets[:]
    print(alphabets)
    # out: []

    # 6
    lst = [4, 5, 7] * 3 + [8]
    print(len(lst))
    # out: 10

    # 7
    # my_color = 'Yellow'
    # my_color[5] = 's'
    # print(my_color)
    # out: TypeError: 'str' object does not support item assignment

    # 8
    my_values = (1, 2, 3, 4)
    my_values = my_values[1:-1]
    my_values = my_values[1]
    print(my_values)
    # out: 3
