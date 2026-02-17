maths=int(input('enter maths marks:'))
sci=int(input('enter maths sci:'))
hindi=int(input('enter maths hindi:'))

def percentage(maths,sci,hindi):
 return (maths+sci+hindi)/3
    
jaydeep=percentage(maths,sci,hindi)
#  return stores the value
print('jaydeep scored:',jaydeep)

meet=jaydeep+10

print('meet scored:',meet)