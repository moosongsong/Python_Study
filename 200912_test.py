total = 0
for n in range(1,20,2):
    total = total + sum(range(1, n+1, 2))
print(total)




import random

random.seed(100)
T = ['가위', '바위', '보']

for n in range(5):
    user = int(input("0 가위, 1 바위, 2 보를 입력하세요 : "))
    computer = random.randint(0,2)
    if (user == 2 and computer == 0) or (computer > user):
        print('컴퓨터 {}, 사용자 {} : 컴퓨터가 이겼습니다.'.format(T[computer], T[user]))
    elif (user == 0 and computer == 2) or (user > computer):
        print('컴퓨터 {}, 사용자 {} : 사용자가 이겼습니다.'.format(T[computer], T[user]))
    else:
        print('컴퓨터 {}, 사용자 {} : 비겼습니다.'.format(T[computer], T[user]))




import random

random.seed(100)

count = 0
computer = random.randint(1, 100)
user = 0;
print(computer)
while True:
    user = int(input("숫자를 입력하세요 : "))
    count = count + 1
    if user == computer:
        break
    elif user < computer:
        print("더 큰 수를 입력세요.")
    elif user > computer:
        print("더 작은 수를 입력세요.")

print('정답은 {}입니다. {}번 만에 정답을 맞추었습니다.'.format(computer, count))




a = int(input('Input the first num : '))
b = int(input('Input the second num : '))

start = 0
if a%2 == 1:
    start = a
else:
    start = a+1

result = sum(range(start, b+1, 2))

print(result)




for n in range(4):
    result = input('Input two int values and an operator : ')
    t = result.split(' ')
    temp = t[0]+t[2]+t[1]
    print(eval(temp))
