a=4
m=0
def tst(a):   
 a=a+5
 print('local\\private inside',a)

tst(a)
print('global outside',a)

#  call value not change original