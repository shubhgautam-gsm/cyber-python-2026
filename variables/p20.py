a=float(input('write value of a'))
b=float(input('write value of b'))
 
user=None
# + (Addition)

user=str(input('write add | sub | mult | div | pow | floor :'))
if user == 'add':
 print('add = ',a+b)
elif user == 'sub':
 print('sub = ',a-b)
elif user == 'mult':
 print('mult = ',a*b)
elif user == 'div':
 print('div = ',a/b)
elif user == 'pow':
  print('pow = ',a**b) #ex 2 ** 3 = 2 * 2 * 2
elif user == 'floor':
  print('floor = ',a//b) #ex 2 // 3  6
else:
  print('invalid input') 