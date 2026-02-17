# main.py
import calc2 as cal
import importlib # IN BUILT

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Div= ", cal.add(a,b)) #
# Reload the module
cal = importlib.reload(cal) # accept changes during run time if any changes made at code

# Try using the function again after reloading
print("Modified Div= ", cal.add(a, b))
