a = 10
b = 20
c = a + b
# 10 + 20 = 30
print(a,'+', b, '=', c)

# str.format() : 메서드
print( '{} + {} = {}'.format(a, b, c) )
# str % : 연산
print( '%d + %d = %d' % (a, b, c) )
# f-string
print( f'{a} + {b} = {c}' )
