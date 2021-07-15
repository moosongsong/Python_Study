# 동작 결과 생성되는 item의 개수는?
a = [ x*y for x in range(2, 10)
             for y in range(1, 10) ]
b = { x*y for x in range(2, 10) for y in range(1, 10) }
print(a)
print(b)
print('length of a : ', len(a))
print('length of b : ', len(b))

# name을 key, score를 value로 하는 dict 를 생성
# 결과 : { 'Sam' : 91, 'Merry' : 96, 'Tom' : 85 }
name  = ['Sam', 'John', 'Merry', 'Tom']
score = [90.5, 75.2, 95.8, 85.3]

r = { k:int(v+0.5)
      for k, v in zip(name, score)
      if v >= 80.0 }
print(r)

# () [] {}
