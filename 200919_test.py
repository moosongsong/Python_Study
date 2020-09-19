d = {'A': 1, 'B':2 , 'C' :3 }
#a = d['D']

try :
    a = d['D']
except:
    import traceback
    print(traceback.format_exc())
    a = -1

print(a)

b = d.get('D', -1)
print(b)

tot = 0
b = d.get('D', -1)
if (b != -1)
    tot += d['D'] 
