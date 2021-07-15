
a = (1, 2, [3, 4], 5, 6, 7, 8)

if 0 :
    b = a[2:5]    
    print(id(a), id(b))
    for x in a :
        print(id(x), x)
    for x in b :
        print(id(x), x)

    b[0][1] = 100
    print(b[0][1], a)
    
if 0:
    print(a[:5])
    print(a[2:])
    print(a[::-1])
    print(a[::2])
    print(a[1::2])

if 0:  
    a = list(range(1, 11))
    print(id(a), a)

    print(a[1::2])
    a[1::2] = [0]*len(a[1::2])
    print(id(a), a)

    a[:] = list(range(1, 5))
    print(id(a), a)
