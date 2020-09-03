#from MyModules import m1
#from MyModules.m1 import add, sub
import MyModules.m1 as m

a = m.add(30, 20)
b = m.sub(30, 10)
print(a, b)

if __name__ == '__main__' :
    print(__name__)
