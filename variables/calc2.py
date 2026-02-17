a=float(input('write value of a'))
b=float(input('write value of b'))
 
user=None
# + (Addition)

user=str(input('write add | sub | mult | div | add & sub "1" || mult & div "2":'))


if user == 'add':
 print('add = ',a+b)
elif user == 'sub':
 print('sub = ',a-b)
elif user == 'mult':
 print('mult = ',a*b)
elif user == 'div':
 print('div = ',a/b)
elif user == '1':
 print('add=',a+b,'sub=',a-b)
elif user == '2':
 print('mult=',a*b,'div=',a/b)

else:
  print('invalid input')  
  
  
  
