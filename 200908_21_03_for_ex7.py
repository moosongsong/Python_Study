# 2 ~ 9의 숫자에서 prime number를 구분하는 프로그램을 작성하라
# for ~ else문을 사용한다
# prime number 란
# '1과 자신이외의 다른 수로 나누어 떨어지지 않는 수' 이다
import math
if 0:
    for n in range(2, 10):
        print(n, int(math.sqrt(n)) + 1)
    
if 1:
    for n in range(2, 10):
        for x in range(2, int(math.sqrt(n)) + 1):
            # 반복 중간에 종료할 수 있는 조건 ? break
            if not n % x :
                print(f'{n} equals {x} * {n//x}')
                break
        else:
            print(n, 'is a prime number')    
