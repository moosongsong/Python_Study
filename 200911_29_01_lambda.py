
def add1(a, b):
    return a + b
x = add1(10, 20)

add2 = lambda a, b : a + b
y = add2(10, 20)

y = (lambda a, b : a + b)(10, 20)
print(x, y)

