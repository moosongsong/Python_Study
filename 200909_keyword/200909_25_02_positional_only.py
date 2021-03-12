
def func1(a, /):
    print(a)

def func2(a, b=20, /):
    print(a, b)

func1(10)
#func1(a=20)
# 이렇게 사용이 불가하다. position only 이기 때문이다.
func2(10)
func2(10, 30)
