age = 23
name = 'Julie'
height = 160.5

print(f'My name is {name}. I\'m {age} years old. \
My height is {height}.')

data1 = [23, 1000,'Julie','A+', 160.5]
# [23, 'Julie', 160.5] => unpack => 23, 'Julie', 160.5
# argument unpack : *data1
print('My name is {2}. I\'m {0} years old. \
My height is {4}.'.format(*data1))


data2 = {'height' : 160.5, 'age' : 23, 'name':'Julie' }
# {'height' : 160.5, 'age' : 23}
# => unpack => height=160.5, age=23, name='Julie'
# argument unpack : **data2
print('My name is {name}. I\'m {age} years old. \
My height is {height}.'.format(**data2) )
