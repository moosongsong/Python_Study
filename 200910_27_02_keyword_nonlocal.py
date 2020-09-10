
if 0: 
    a = 100
    def outerFunction():
        a = 200
        def innerFunction():
            a = a + 1
            
        innerFunction()
        print(a)

    outerFunction()

if 0: 
    a = 100
    def outerFunction():
        a = 200
        def innerFunction():
            nonlocal a
            a = a + 1
            
        innerFunction()
        print(d['a'])
        

if 0: 
    a = 100
    def outerFunction():
        d = {'a' : 200}
        def innerFunction():
            d['a'] += 1
            
        innerFunction()
        print(d['a'])

    outerFunction()
