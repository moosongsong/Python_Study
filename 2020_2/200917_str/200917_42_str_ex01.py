
msg = ' Good   morning! '
print(msg.split('o'))
# [' G','','d   m','rning! ']
# 구분자 나오면 : 닫고 - 구분자 지우고 - 콤마 - 열고

print(msg.split(' '))
# ['','Good','','','morning!','']
print(msg.split( ))  # whitespace, [ \t\r\f\n\v]
# ['Good','morning!']
print( ' '.join(msg.split()))
print( ':'.join(msg.split()))

