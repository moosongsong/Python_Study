import datetime

a = range(1000)
start = datetime.datetime.now()
data = []
for i in a :
    data.append(str(i))
print("\n".join(data))
end = datetime.datetime.now()
t1 = end-start

start = datetime.datetime.now()
for i in a :
    print(i)   
end = datetime.datetime.now()
t2 = end-start

print(t1, "list-append, join")
print(t2, "for")


