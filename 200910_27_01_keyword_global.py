  
if 0:
    a = 100
    def myFunction():
        a = a + 1

    myFunction()
    print(a)
    
if 0:
    a = 100
    def myFunction():
        global a, b
        a = a + 1
        b = 10
        
    myFunction()
    print(a, b)

if 0:
    a = 100
    def myFunction():
        global a
        a = a + 1

    myFunction()
    print(a)

if 0:
    a = [100]
    def myFunction():
        a[0] += 1

    myFunction();
    print(a[0])

if 0:
    d = {'a' : 100}
    def myFunction():
        d['a'] += 1

    myFunction();
    print(d['a'])
