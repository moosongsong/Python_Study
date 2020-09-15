
a = [0] * 3
#b = [[0]] * 3
#c = [[0]*3] * 3
b = [ [0] for _ in range(3) ]
c = [ [0]*3 for _ in range(3) ]
print(a, b, c, sep='\n')

for x in b :
    print(id(x), x)

for x in c :
    print(id(x), x)
    
a[0] = 10
b[0][0] = 10
c[0][0] = 10
print(a, b, c, sep='\n')
