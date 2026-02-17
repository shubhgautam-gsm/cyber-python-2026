class Details:
 age = 22
 name = "Phill"


details = Details()

print('# GET ATTRIBUTE')
#GETATTRIBUTE    function , key 
print('The age is:', getattr(details,"age")) #opt1
# print('The age is:', getattr(details,"rollno", "age"))
# not take multiple values in getattr()
print('The age is:', details.age)#opt2 get value of key




# SETATTRIBUTE
print('# SET ATTRIBUTE')

details.age=62 #set 22 to 62 opt1
setattr(details, "name", "John") #opt2
print('The name is:', details.age)
print('The age is:', details.name)# updated value of key



# DEL ATTRIBUTE
print('# DEL ATTRIBUTE')
del details.age #opt1
delattr(details,"name") #opt1

print('The age is:', details.age) # will print None as it has been deleted.
print('The name is:', details.name) # will print None as it has been deleted.
