# Python translate() method
# Declaring table and variables
# can be use in encryption because ascii value change so char change ex.a is 97 but after
# 103 instead of 'a'  'g' is print
table = { 97 : 103, 111 : 112, 117 : None }
str = "Hello javatpoint"
# Calling function
str2 = str.translate(table)
# Displaying result
print(str)