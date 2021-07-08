def solve1():
    num = input("정수를 입력하세요")
    for i in range(int(num)):
        for j in range(i * 2 + 1):
            print("*", end='')
        print()


def solve2():
    num = int(input("홀수를 입력하세요"))
    if num % 2 == 0:
        print("None")
        return
    for i in range(num):
        for j in range(i):
            print(f"{j + 1}", end='')
        print(i + 1, end='')
        for j in range(i, 0, -1):
            print(f"{j}", end='')
        print()


def solve3():
    num = int(input("홀수를 입력하세요"))
    if num % 2 == 0:
        print("None")
        return
    for i in range(num):
        if i < num // 2 + 1:
            for j in range(1, i + 1):
                print(f"{j}", end='')
            for j in range(i + 1, 0, -1):
                print(f"{j}", end='')
        else:
            for j in range(1, num - i):
                print(f"{j}", end='')
            for j in range(num - i, 0, -1):
                print(f"{j}", end='')
        print()


def solve4():
    num = input("정수를 입력하세요")
    result = 0
    for i in range(int(num)):
        result += i + 1
    print(result)


def solveRe():
    num = int(input("정수 입력"))
    count = 0
    flag = True
    first = 0
    temp = num
    while flag:
        if count >= 100:
            flag = False
            break

        square_sum = 0
        for i in str(temp):
            square_sum += int(i) * int(i)

        if first == 0:
            first = square_sum
        elif first == square_sum:
            break
        temp = square_sum
        count += 1
    if not flag:
        print("over 100s")
    else:
        print(count)


solveRe()
