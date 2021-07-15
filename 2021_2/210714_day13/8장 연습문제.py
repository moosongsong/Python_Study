# 1
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

# 2
print(e2f.get('walrus'))

# 3
# f2e = {}
# for key, value in e2f.items():
#     f2e[value] = key
f2e = {value: key for key, value in e2f.items()}
print(f2e)

# 4
print(f2e.get('chien'))

# 5
for key in e2f.keys():
    print(key)

# 6
life = {'animals': {'cats': 'Henri',
                    'octopi': 'Grumpy',
                    'enus': 'Lucy'},
        'plants': {},
        'other': {}
        }

# 7
print(life.keys())

# 8
print(list(life['animals'].keys()))

# 9
print(life['animals'].get('cats'))

# 10
squares = {iter_num: (iter_num * iter_num) for iter_num in range(10)}
print(squares)

# 11
odd = {value for value in range(1, 10, 2)}
# odd = {value for value in range(10) if value % 2 == 1}
print(odd)

# 12
titles = ['optimist', 'pessimist', 'troll']
plots = ['The glass is half full', 'The glass is half empty', 'How did tou get a glass?']

# 13
movies = dict(zip(titles, plots))
print(movies)
