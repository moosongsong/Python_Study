# 색상 값은 어떻게 나타낼까?
# 대부분 4Byte로 Alpha, Red, Green, Blue를 이용하여 나타낸다.
# 색상값이 AABBCCDD일때 각각 1바이트씩 분리하고 다시 결합해 보자
# 2진수 4자리는 16진수 1자리이다. 1Byte는 8Bit이므로 16진수 2자리로 표현 가능하다.
# and 연산은 값을 지울 때 사용합니다.
# 0으로 &연산하면 0이고 1로 &연산하면 통과.
# or 연산은 값을 설정할 때 사용.
# 0으로 |연산하면 통과이고 1로 |연산하면 1이 결과로 나옴.

# 색상분리
color = 0xAABBCCDD
alpha = color >> 24 & 0xFF
red = color >> 16 & 0xFF
green = color >> 8 & 0xFF
blue = color & 0xFF

print(color, hex(color))
print(alpha, hex(alpha))
print(red, hex(red))
print(green, hex(green))
print(blue, hex(blue))

# 색상 결합
color2 = 0
print(color2, hex(color2))
color2 = color2 | alpha << 24
print(color2, hex(color2))
color2 = color2 | red << 16
print(color2, hex(color2))
color2 = color2 | green << 8
print(color2, hex(color2))
color2 = color2 | blue
print(color2, hex(color2))

# red값 만 삭제
color2 = color2 & 0xFF00FFFF
print(color2, hex(color2))

# red값을 56으로 설정
color2 = color2 | 0x00560000
print(color2, hex(color2))