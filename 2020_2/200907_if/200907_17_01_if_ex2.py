# 한 개의 정수를 입력 받아 num 에 저장하고,
# num이 2의 배수면 2, 3의 배수면 3, 5의 배수면 5를
# 2,3,5 배수가 아니면 0을 출력한다
# 단, 2의 배수면서 3의 배수이면 2의 배수로 출력,
# 3의 배수면서 5의 배수면 3을 출력한다

# I - P - O
while True :
    num = int(input('Input a number : '))
# if statement
# Alt + 3, Alt + 4 : Comment
##    if not num % 2 : result = 2
##    elif not num % 3 : result = 3
##    elif not num % 5 : result = 5
##    else : result = 0

# conditional expression (if expression)
    result = 2 if not num % 2 else \
             3 if not num % 3 else \
             5 if not num % 5 else 0

    print(result)
