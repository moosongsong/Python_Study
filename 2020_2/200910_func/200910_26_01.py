# Name Resolution
# read : local - global - built-in
import pprint

x = sum(range(1, 11))
print(x)

sum = 0
for x in range(1, 11):
    sum += x
print(sum)

del sum
x = sum(range(1, 11))
print(x)

if 0:
    a = 10
    pprint.pprint(globals())
    def func():
        a = 20
        print(a)
        print(locals())
        print(b)
        
    func()
