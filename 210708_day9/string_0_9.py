thing = 'wereduck'
place = 'werepond'

print(f'The {thing} is in the {place}')

print(f'The {thing.capitalize()} is in the {place.rjust(20)}')

print(f'The {thing:>20} is in the {place:.^20}')

print(f'The {thing:>20} is in the a1a2a3a4a5')

print(f'The {thing:<20} is in the a1a2a3a4a5')

print(f'The command order is in the {place:.^20}')

print(f'{thing =}, {place = }')

print(f'{thing[-4:] =}, {place.title() = }')

print(f'{thing = :>4.4}')