# 한 줄로 입력된 정수 3개를 입력 받아 합을 구하여 출력하라
# 단, str.split() 메서드는 argument를 입력하지 않으면 
# str을 공백을 기준으로 분리하여 문자열 리스트를 반환한다
# 예
# Input three numbers : 10 20 30
# 60
'''
data = input('Input three numbers : ')
a = data.split()
print(a)
b = list(map(int, a))
print(b)
print(sum(b))
'''
data = input('Input three numbers : ').split()
print(sum(map(int, data)))
