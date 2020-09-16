
data = ('kiwi','apple','orange','banana', 'melon')
a = sorted(data)
print(data, a, sep='\n')

data = [('apple', 'red', 500),
        ('kiwi', 'brown', 300),
        ('banana', 'yellow', 300)]
b = sorted(data, )
c = sorted(data, key=lambda x: x[0])
d = sorted(data, key=lambda x: x[1])
e = sorted(data, key=lambda x: (x[2], x[1]))
print(b, c, d, e, sep='\n')
