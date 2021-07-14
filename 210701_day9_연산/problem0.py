inputValue = 4

inputStr = str(inputValue)

toSquare = 0
count = 0

while True:
    for i in range(0, len(inputStr)):
        toVal = int(inputStr[i])
        toSquare += toVal * toVal
    count += 1
    inputStr = str(toSquare)
    if toSquare == inputValue:
        break
    toSquare = 0
print(count)