# UnboundLocalError

value = 3
def add_num(lvalue,num=1):
    return lvalue + num

value = add_num(value)
print(value)

# function object -> bytecode, varnames
# varnames -> parameter(num), value
# function all -> local namespace 생성, varnames
