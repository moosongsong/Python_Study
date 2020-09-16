import copy

def printIDs(*arr):
  for t in arr:
    ids0 = id(t)
    ids1 = [ id(r) for r in t ]
    ids2 = [ id(x) for r in t for x in r ]

    print(ids0, ids1, ids2, sep='\n')
    
a = [[1,2],[4,5]]
b = a.copy()
c = copy.deepcopy(a)
d = a
printIDs(a, b, c, d)

a[0] = 100
#a[0][0] = 10
print(a, b, c, d, sep='\n')
