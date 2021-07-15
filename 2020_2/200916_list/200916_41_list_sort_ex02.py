

if 0:
    alphabet = ['A', 'z', 'a', 'Z', 'c']
    print(f'alphabet = {alphabet}')
    alphabet.sort(key=str.lower)
    print(f'alphabet = {alphabet}')

    alphabet.sort(key= lambda x : (str.lower(x), x)) # 2차 정렬입니다!
    print(f'alphabet = {alphabet}')
