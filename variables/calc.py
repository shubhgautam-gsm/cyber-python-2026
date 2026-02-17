a=float(input('write value of a'))
b=float(input('write value of b'))
 
user=None
# + (Addition)

user=str(input('write add | sub | mult | div:'))
if user == 'add':
 print('add = ',a+b)
elif user == 'sub':
 print('sub = ',a-b)
elif user == 'mult':
 print('mult = ',a*b)
elif user == 'div':
 print('div = ',a/b)
else:
  print('invalid input')  