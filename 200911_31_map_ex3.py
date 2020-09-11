# map함수에 여러 개의 parameter를 갖는 함수 사용 방법

# a,b,c의 같은 위치 item 중 가장 큰 값을 갖는 list 작성
# 출력 예) [6, 7, 5, 7, 8]
a = [6, 2, 3, 4, 5]
b = [2, 3, 5, 7, 1]
c = [5, 7, 2, 3, 8]

r = list(map(max, a, b, c))
print(r)
#r[0] = max(a[0], b[0], c[0])

r = list(map(max, zip(a,b,c)))
print(r)
#r[0] = max( (a[0], b[0], c[0]))


    
