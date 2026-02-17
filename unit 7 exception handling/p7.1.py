try:
 age = int(input("Enter the age:"))
#ValueError = datatype int points(floats),strings not allowed
#2 condi gen ValueError
 if(age<18):
  raise ValueError
 print("the age is valid")
#ValueError = datatype int points(floats),strings not allowed
#3 condi gen ValueError
except Exception as e:
 print("The age is not valid",e)