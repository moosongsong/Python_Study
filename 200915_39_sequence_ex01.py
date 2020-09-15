# 최대값 구하기
# 다음 조건에 따라 값을 구하는 프로그램을 작성하여 보자
# - 9개의 서로 다른 자연수가 한 줄에 공백으로 구분되어 주어진다
# - 9개의 값 중 최대값을 찾고
#   그 값이 몇 번째 수인지 구하여 출력한다
# - 첫째 줄에 최대값을 출력하고,
#   둘째 줄에 최대값이 몇 번째 수인지 출력한다
# 예)
# 3 29 38 12 57 74 40 85 61
# 85
# 8
a = list(map(int, input().split()))
print(a)
maxValue = max(a)
maxIndex = a.index(maxValue) + 1
print(maxValue)
print(maxIndex)
#print(max(a))
#print(a.index(max(a)) + 1)
