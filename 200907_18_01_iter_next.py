
a = (10, 20, 30) # a : tuple, iterable, sequence, immutable
b = iter(a)      # b : iterator  
print( next(b) ) # 10 
print( next(b) ) # 20
print( next(b) ) # 30
try:
    print( next(b) ) # StopIteration Exception
except:
    print("done")
    
for x in (10, 20, 30):
    print(x)

# iterable : iter(iterable) -> iterator
# next(iterator) -> next item
# target : next item -> binding, operation
# iteration
# StopIteration Exception -> for statement 종료 





