# 점수를 입력하면 학점을 출력하는 프로그램을 설계하라
# 0~100점의 점수에 대해 다음 기준을 적용하여 학점을 출력한다
# 단, 0점 미만, 100점 초과 점수에 대해서는 “Error” 를 출력한다
# 학점 기준
# 100~90 -> A, 89~80 -> B, 79~70 -> C, 69~60 -> D, 59~0 -> F

# I - P - O
while True :
    score = int(input('Input a score : '))

    if score < 0 or score > 100 : grade = 'Error'
    elif score >= 90 : grade = 'A'
    elif score >= 80 : grade = 'B'
    elif score >= 70 : grade = 'C'
    elif score >= 60 : grade = 'D'
    else : grade = 'F'

    print(grade)
