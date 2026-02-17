try:
 print(x)
 
except Exception as e:
    print('U FORGOT SOMETHING',e)# <-- will never run if error occurs above

print('i am after after')