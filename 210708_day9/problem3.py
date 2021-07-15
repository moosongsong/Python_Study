inputValue = 11

q, r = divmod(inputValue, 2)

if r == 0:
    print("None")

else:
    for i in range(1, q+r+1):
        for j in range(1, i+1):
            print(j, end="")

        for j in range(i-1, 0, -1):
            print(j, end="")

        print()

    for i in range(q, 0, -1):
        for j in range(1, i+1):
            print(j, end="")

        for j in range(i-1, 0, -1):
            print(j, end="")

        print()


