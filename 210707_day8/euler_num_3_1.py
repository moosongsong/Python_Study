import math

count = 2

while True:
    isprime = True

    for x in range(2, int(math.sqrt(count) + 1)):
        if count % x == 0:
            isprime = False
            break

    if isprime:
        print(count)

    count += 1

else:
    print("Returning while statement")