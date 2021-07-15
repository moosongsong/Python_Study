thing = 'woodchuck'
place = 'lake'

print('{}'.format(thing))

print('The {} is in the {}.'.format(thing, place))

formatted_result = 'The {} is in the {}.'.format(thing, place)

print(formatted_result)

print('The {1} is in the {0}.'.format(place, thing))

print('The {thing} is in the {place}.'.format(thing='duck', place='bathtub'))

d = {'thing': 'duck', 'place': 'bathtub'}

print('The {0[thing]} is in the {0[place]}.'.format(d))