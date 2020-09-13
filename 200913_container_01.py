# 묶음 기호를 사용한 Container 생성

# set 객체 생성 
s1 = { 1, 2, 1, 2, True, 3.5, (1, 2), "Julie" }
print(s1)
s1 = { 1, True, 1.0 }
s2 = { False, 0.0, 0 }
s3 = { 10.0, 10 }
print(s1, s2, s3)
print( {1, 2, 3} == {3, 1, 2} )
print( {1, 2, 3} , {3, 1, 2} )
#s2 = { [1, 2], 3 }
#s3 = { {1, 2}, 3 }
#s4 = { {'name':'happy'}, 3}

# dict 객체 생성 
d1 = { 10   : 'ten',
       3.14 : 'pi',
       True : 1,
       'kiwi' : 'green',
       ('brown', 12) : 'my hair color'}

#d2 = { [1, 2] : "nope" }
#d3 = { {1, 2} : "nope"  }
#d4 = { {'name':'happy'} : "nope" }
print(d1)
print( {1:10, 2:20}, {2:20, 1:10} )
print( {1:10, 2:20} == {2:20, 1:10} )
