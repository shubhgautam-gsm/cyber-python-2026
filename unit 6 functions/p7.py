#defining the function
def change_string (string1):
 string1 = string1 + " Hows you"
#  it remains local/privates
 print("printing the string inside function :",string1)

string1 = "Hi I am there"
#calling the function
change_string(string1)
print("printing the string outside function :",string1)
# call by value


#a=4 global variable
# {
#  a=a+5      # local variable / private    
#  print(a) ans 9
# }
#print(a) ans 4