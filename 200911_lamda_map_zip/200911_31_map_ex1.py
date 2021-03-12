# 모든 item 을 정수로 변경하기
data = ['10', '20', '30', '40']
#print(int(data[0]), float(data[0]))
b = map(int, data)
for x in b:
    print(type(x), x)
#c = list(b)
#print(c)
c = list(map(int, data))
print(c)

# 문자열을 분리하고, 불필요한 앞/뒤의 공백 삭제하기
s = 'Julie | 010-123-1234 | 30 | F'
b = map(str.strip, s.split('|'))
c = list(b)
print(c)
