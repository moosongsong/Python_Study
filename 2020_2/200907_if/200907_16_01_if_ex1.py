# 하나의 문자를 입력 받아 a 에 저장하고
# a 가  알파벳 'f' ~ 'o' 사이의 알파벳인 경우 'YES'
# 아닌 경우 'NO'를 출력하는 프로그램을 작성한다

# Input - Process - Output

a = input('Input a character : ')

# ctrl + '['  : DEDENT
if 0 :  
    if 'f' <= a <= 'o' :
        msg = 'YES'
    else :
        msg = 'NO'

# conditional expression
# 'YES' if condition else 'NO'
msg = 'YES' if 'f' <= a <= 'o' else 'NO'
print(msg)    
