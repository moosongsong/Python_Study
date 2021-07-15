a = ('apple', 'banana', 'orange')
b = [ 1, 3, 4, 7, 9 ]
c = {6, 4, 2, 10, 8} # { 2, 4, 6, 8, 10 } # set은 순서 개념이 없다 
d = {'color':'red', 'price': 5000 }
e = [ (1, 2, 3), (4, 5, 6), (7, 8, 9) ]

for x in e :
    print(*x, end=', ') # argument unpack
    
for x, y, z in e :
    print(x, y, z, end=', ')

# dict
# d.keys(), d.values(),  d.items()
