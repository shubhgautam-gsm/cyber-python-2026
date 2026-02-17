# The python format() function returns a formatted representation of the given value.
# integer

user=float(input("Entervalue: "))
# case1 
if('.' in user):
    phone=user.replace('.', '')
    print(phone)
# #case 2 
# phone=format(user, "d") #i want without points because ph no
# print(phone)



