# 전체 item의 합에 대한 각 item의 비율 list 생성
# 출력 예) [13, 6, 26, 13, 40]
a = [ 100, 50, 200, 100, 300 ]
t = sum(a)
r = [ int(x/t*100) for x in a ]
print(r)

# 모음을 제외한 문자 list 생성
a = 'watermelon'
b = 'aeiou'
r = [ x for x in a if x not in b ]
print(r)

# integer type인 item만 대상으로 제곱한 값의 list생성  
a = [-1, 'a', '1', 1, 2, 'red', 3.4, True]
r = [ x**2 for x in a if type(x) is int ]
print(r)

