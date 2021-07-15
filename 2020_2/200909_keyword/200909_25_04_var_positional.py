# var-positional parameter

def getSum(*data): #tuple 이다.
    print(type(data), len(data))
    return sum(data) #tuple 에 있는거 다 계산이 가능하다.

r = getSum(1,2,3,4,5,6,7,8,9,10)
print(r)

r = getSum(10, 20, 30)
print(r)

r = getSum()
print(r)
