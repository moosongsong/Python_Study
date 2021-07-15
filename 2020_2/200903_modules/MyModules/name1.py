import sys

a = 100
b = 200

class A:
    def __init__(self, value):
        self.value = 10

    def add(self, other):
        return self.value + other

def add(a, b):
    return a + b

x = A(10)
print(x.add(20))
print(add(a, b))

