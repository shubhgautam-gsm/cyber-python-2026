age = int(input("Enter your age? "))
if age>=18 and age<=100:
 print("You are eligible to vote !!")
elif age>=0 and age<18:
 print("Sorry! you have to wait !!")
elif age>100 or age<0:
 print("out of range age given")
else:
    print("Invalid age")

 