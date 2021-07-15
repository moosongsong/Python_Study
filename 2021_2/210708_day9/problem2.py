inputValue = 5

if inputValue % 2 == 0:
    print("None")

else:
    for i in range(1, inputValue+1):
        for j in range(1, i+1):
            print(j, end="")

        for j in range(i-1, 0, -1):
            print(j, end="")



