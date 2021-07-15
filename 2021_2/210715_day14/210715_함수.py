def do_nothing():
    pass


def make_a_sound():
    print("quack")


def agree():
    return True


def echo(anything):
    return anything + " " + anything


def not_thinking():
    return None


print(do_nothing())
print(make_a_sound())
print(agree())
print(echo("hello"))
print(not_thinking())


#
# print(whatis(None))
# print(whatis(True))
# print(whatis(False))
# print(whatis(0))
# print(whatis(0.0))
# print(whatis(''))
# print(whatis(""))
# print(whatis(''''''))
# print(whatis(()))
# print(whatis([]))
# print(whatis({}))
# print(whatis(set()))
# print(whatis(0.00001))
# print(whatis([0]))
# print(whatis(['']))
# print(whatis(' '))


def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


print(menu('beef', 'bagel', 'Bordeaux'))

print(menu(entree='beef', dessert='bagel', wine='Bordeaux'))

print(menu('frontenac', dessert='flan', entree='fish'))


def print_args(*args):
    print(f"Positional tuple: {args}")


print_args()

print_args(3, 2, 1, "wait!", "uh…")


def print_kwargs(**kwargs):
    print('Keyword args:', kwargs)


print_kwargs()

print_kwargs(wine='merlot', entrée='mutton', dessert='macaroon')


def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)


data = ['a', 'b', 'c', 'd', 'e', 'f']

print_data(data)
print("-------------")
print_data(data, start=4)
print("-------------")
print_data(data, end=2)


outside = ['one', 'fine', 'day']
def mangle(arg):
    arg[1] = 'terrible!'

print(outside)

mangle(outside)
print(outside)
