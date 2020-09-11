# a ** 2
power = lambda a : a ** 2
print(power(10))

def add(a, b):
    return a + b
'''
print(type(add), add.__name__)
print(type(power), power.__name__)
power.__name__ = 'power'
print(power.__name__)
'''
# a + b
add2 = lambda a, b : a + b
print(add2(10, 20))

# a // b, a % b
mydivmod = lambda a, b : (a//b, a%b)
print(mydivmod(10, 3))

func = lambda : 100
print(func())

y = 10
func = lambda x : x + y
print(func(10))

