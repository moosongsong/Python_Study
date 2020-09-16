def printobj(a):
    for x in a:
        print(x)
        
f1 = [('apple','red', 500),
      ('kiwi','brown', 300),
      ('banana','yellow', 300)]
f2 = sorted(f1)
f3 = sorted(f1, key = lambda x : x[1])
f4 = sorted(f1, key = lambda x : x[2])
f5 = sorted(f1, key = lambda x : (x[2], x[0]) )
#printobj(f5)

d1 = [{'x':2, 'y':3}, {'x':4, 'y':1},
      {'x':3, 'y':2}, {'x':1, 'y':4}]
#dx = sorted(d1)
d2 = sorted(d1, key = lambda x : x['y'] )
printobj(d2)
