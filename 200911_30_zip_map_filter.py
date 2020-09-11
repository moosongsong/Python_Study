# zip
a = (82, 52, 1)      
b = ('Korea', 'Maxico', 'USA')
c = zip(a, b)
print(type(c))

print(next(c))
for x in c:
    print(x, type(x))

c = zip(a, b)
for x in c:
    print(type(x), x)

# map
a = ['Korea', 'Maxico', 'USA', 'Japan', 'China']
b = map(len, a)
for x, y in zip(a, b) :
    print(x, y)

import sys
print(sys.getsizeof(a))
print(sys.getsizeof(map(len,a)))

    
# filter
# 문자열의 길이가 홀수 인 것
countries = ['Korea', 'Maxico', 'USA']
a = filter(lambda x : len(x)%2, countries)
for x in a :
    print(x)

b = list(filter(lambda x : len(x)%2, countries) )
print(b)


