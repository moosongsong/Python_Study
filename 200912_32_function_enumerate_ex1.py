# a에 enumerate를 적용하여 결과를 관찰하라
a = ['Korea', 'Maxico', 'USA']
b = list(enumerate(a))
print(b)

for idx, value in enumerate(a):
    print(idx, value)
    
# name을 사용하여 다음과 같은 dict를 생성하라 
# {100:'Kim', 101:'Park', 102:'Choi', 103:'Lee', 104:'Ann'}
name = ['Kim', 'Park', 'Choi', 'Lee', 'Ann']
b = dict(enumerate(name,100))
print(b)



