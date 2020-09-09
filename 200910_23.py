def add(a,b):
  print(locals())
  c = a+b
  return c

r = add(10, 20)
print(r)
print(globals())

import dis

print(add.__code__.co_varnames)
dis.dis(add)

########################################

def getYesNo(a):
  return 'YES' if 'f' <= a <= 'o' else 'NO'
  
def getTimes(num):
  if not num%2 : result = 2
  elif not num%3 : result = 3
  elif not num%5 : result = 5
  else : result = 0
  return result

import dis
dis.dis(getTimes)

a = input('Input a character : ')
msg = getYesNo(a)
print(msg)

num = int(input('input number :'))
result = getTimes(num)
print(result)
