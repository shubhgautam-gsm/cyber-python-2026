



password='dddffffffrerfx4s'

length=len(password) #STEP 1

password=password[-3:] #STEP 2  LAST 3 CHAR
password=password.rjust(length, 'x')
# print(length)
print(password)


