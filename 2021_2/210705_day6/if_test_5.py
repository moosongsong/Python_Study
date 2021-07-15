disaster = False
print("globals are \n"+ str(globals()))
print("locals are \n"+ str(locals()))

if disaster:
    variable_in_if = 0
    print("wow")
    print("locals in if statement\n" + str(locals()))

else:
    print("wow! not disaster")

print("locals at outer if statement\n" + str(locals()))
