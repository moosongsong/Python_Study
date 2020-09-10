a = range(10)
b = range(1, 101)
c = range(1, 10001, 2)

print(a, b, c)
print(tuple(a), list(b))

import sys

for x in a, b, c:
    print(sys.getsizeof(x))

for x in a:
    print(x)

print(sys.getsizeof( tuple(c) ))
print(sys.getsizeof( list(c) ))
