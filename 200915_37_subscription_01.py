
a = (1, 2, [3, 4], 5, 6, 7, 8, 9)
print(a[0])
print(a[2])
print(a[-1])
print(a[-2])
print(a[2][1])

a = ( {1, 2, 3}, (3.14, 'love', 10), [4, 'hi'] )
print( type(a), a )
print( type(a[1]), a[1])
print( type(a[1][1]), a[1][1] )
print( type(a[2][1][0]), a[2][1][0] )
print( a[-1][-1] )
# a[1][1] = 10  # tuple 'a[1]'
# a[0] = 100  # tuple 'a'
a[-1][0] = 10  # list a[-1]
# a[0][-1] = 4  # set a[0]
# print(a[0][-1]) # set a[0], subscription 불가능
# a[1][1][1] = 'x' # str, a[1][1] 

