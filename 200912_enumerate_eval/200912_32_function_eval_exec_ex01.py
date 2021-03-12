# eval
myList = [1, 2, 3, 4, 5]

a = eval('len(myList)')
print(type(a), a)

# exec
exec('b = 10 + 20')
print(b)
print(globals())
