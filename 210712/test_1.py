def make_list_1():
    temp = list()
    for i in range(1980, 1986, 1):
        temp.append(i)
    print(temp[2])
    temp.sort()
    print(temp[-1])


def make_list_2():
    temp = ['moza', 'cinde', 'sal']
    for item in temp:
        print(item.capitalize())
    print(temp[0].upper())


def make_list_3():
    temp = ['moza', 'cinde', 'sal']
    print(temp[-1].lower()[::-1].capitalize())


def make_list_4():
    temps = [x for x in range(10) if x % 2 == 0]
    for i in temps:
        print(i)


make_list_1()
make_list_2()
make_list_3()
make_list_4()
