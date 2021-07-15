# 비트 연산자(Bitwise Operators)
a = 0b10101010
b = 0b01110011

print('a = ',  a, ":", bin(a))
print('b = ',  b, ":", bin(b))
print('a & b = ',  a & b, ":", bin(a & b))
print('a | b = ',  a | b, ":", bin(a | b))
print('a ^ b = ',  a ^ b, ":", bin(a ^ b))
print('~a = ',  ~a, ":", bin(~a))

a = 0b1
print('a = ', a)
a = a << 1    # * 2
print('a = ', a)
a = a << 1    # * 2
print('a = ', a)
a = a << 3    # * 2**3
print('a = ', a)

a = a >> 1    # / 2
print('a = ', a)
a = a >> 1    # / 2
print('a = ', a)
a = a >> 2    # / 2**2
print('a = ', a)