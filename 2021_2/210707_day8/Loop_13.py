import itertools

def multiply(a, b):
    return a*b

# be careful for the identifier notation of target functions
for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)