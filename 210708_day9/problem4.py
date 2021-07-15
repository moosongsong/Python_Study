inputValue = 10

sumOfTerm = 0
Total = 0

for i in range(1, inputValue+1):
    sumOfTerm = 0
    for j in range(1, i+1):
        sumOfTerm += j
    Total += sumOfTerm

print(Total)