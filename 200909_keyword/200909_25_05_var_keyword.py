# var-keyword parameter

def myPrint(**data): #dictionary 이다.
    print(type(data), len(data))
    for x in data.items():
        print(x, *x)#unpack

myPrint(a=10, b=20, name='Good')
myPrint(x='king', y='prince')
myPrint()
