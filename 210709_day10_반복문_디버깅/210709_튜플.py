import math


def solve1():
    num = int(input("정수 입력>>"))
    total = 0
    ary = list()
    for i in range(num):
        temp = int(input("점수 입력>>"))
        ary.append(temp)
        total += temp
    avg = total / num
    total = 0
    for i in ary:
        total += (i - avg) * (i - avg)
    print(round(total / num, 2))


def solve2():
    num = int(input("정수 입력>>"))
    flag = True
    start = 0
    result = 0
    while flag:
        start += 1
        if start * start > num:
            flag = False
        else:
            result = start
    print(result)


def solve3():
    num = int(input("정수 입력>>"))
    ary = list()
    for i in range(num + 1):
        ary.append(0)

    for i in range(1, num):
        for j in range(i, num, i):
            if ary[j] == 0:
                ary[j] = 1
            else:
                ary[j] = 0
    count = 0
    for i in ary:
        if i == 1:
            count += 1
    print(count)


solve3()
