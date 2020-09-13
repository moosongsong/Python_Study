import time

a = tuple(range(10000000))
b = tuple(range(10000000))
#b = (100,)+tuple(range(9999999))
def funcA() :
   return a == b

c = list(range(10000000))
d = list(range(10000000))
#d[0] = 100
def funcB():
    return c == d

import timeit
x = timeit.timeit(funcA, number = 10)
y = timeit.timeit(funcB, number = 10)

print(x, y)
