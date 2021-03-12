a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
for x in a:
    print(x)
# row/column 전환
for x in zip(*a):
    print(list(x))
    
a = ['Apple', 'Banana', 'Kiwi', 'Orange', 'Melon']
b = [1000, 300, 500, 700, 2500]

# dict 객체 생성
for x in zip(a,b):
    print(x)
d = dict(zip(a,b))
print(d)

print(d['Apple'])
