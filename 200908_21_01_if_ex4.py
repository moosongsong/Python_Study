def func1(n, x):
    if n % x == 0: print('equal')

def func2(n, x):
    if not n % x : print('equal')

import dis

dis.dis(func1)
dis.dis(func2)

# https://docs.python.org/3.7/library/dis.html
