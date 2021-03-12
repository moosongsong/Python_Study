import timeit

n = 1000   
def sumT1():
    tot = 0
    for i in range(1, n+1):
        tot += i  # tot = tot + i
    return tot

def sumT2():
    a = sum(range(1, n))
    return a

def sumT3():
    sol = (n*(n+1))//2
    return sol

print(timeit.timeit(sumT1, number=100000))
print(timeit.timeit(sumT2, number=100000))
print(timeit.timeit(sumT3, number=100000))

#https://nyu-cds.github.io/python-performance-tips/02-timing/

