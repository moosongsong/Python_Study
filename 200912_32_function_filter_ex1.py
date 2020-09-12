# 문자열의 길이가 홀수 인 것
countries = ['Korea', 'Maxico', 'USA']
a = filter(lambda x : len(x)%2, countries)
for x in a :
    print(x)

b = list(filter(lambda x : len(x)%2, countries) )
print(b)

# 6의 배수 인 것
even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18]
a = filter(lambda x : not x%6, even_nums)
print(list(a))

# 'M'으로 시작하는 문자열
names = ['Happy', 'Joy', 'Merry', 'Minky', 'Adam']
a = filter(lambda x : x.startswith('M'), names)
print(list(a))
