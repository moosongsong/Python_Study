
name = 'Julie'
age  = 20

# My name is Julie. My age is 20.
print( 'My name is {}. My age is {}.'.format(name, age) )
# {Julie} is my name, I'm 20 years old.
print( '{{{}}} is my name, I\'m {} years old.'.format(name, age) )

# My name is Julie. My age is 20.
print( 'My name is {1}. My age is {0}.'.format(age, name) )
# My name is Julie. My age is 20.
print( 'My name is {b}. My age is {a}.'.format(a=age, b=name) )

# 20   20  : 왼쪽 정렬
print( '{:<5}{}'.format(age, age))
# 20   20  : 오른쪽 정렬
print( '{}{:>5}'.format(age, age))
# 20   20   20: 가운데 정렬
print( '{}{:^8}{}'.format(age, age, age))
f1   = 1.3456
print( '{:.4}'.format(f1))
# 20    1.345
print( '{}{:9.4}'.format(age, f1))
# 2000020  : 오른쪽 정렬
print( '{}{:0>5}'.format(age, age))
# 123,456,789
print('{:,}'.format(123456789))
