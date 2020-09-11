# 다음과 같은 동작을 하는 myFilter 함수를 작성하라
# 1. parameter : function, iterable 
# 2. argument로 받은 function의 argument로
#    iterable의 각 item을 사용
# 3. 2번의 function 결과가 True인 것에 대해 그 item을 list로 생성
# 4. 3번에서 작성된 list 반환
data = (10, 21, 32, 43, 7, 20)

def myFilter(function, iterable):
    pass

a = myFilter(lambda x : not x%2, data)
print(a)


