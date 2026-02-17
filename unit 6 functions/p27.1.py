# The python exec() function is used for the dynamic execution of Python program which
# can either be a string or object code and it accepts large blocks of code,

code = """

b=5 
print(a+b)
"""  # String containing the code
a=3


exec(code)  # Execute the code
# values= a=3 b=5 a+b