letter = 'o'

vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set)

vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list)

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple)

vowel_string = "aeiou"
print(letter in vowel_string)

vowel_dict = {'a': 'apple',\
              'e': 'elephant',\
              'i': 'impala',\
              'o': 'ocelot',\
              'u': 'unicorn'}
print(letter in vowel_dict)
print('apple' in vowel_dict)

