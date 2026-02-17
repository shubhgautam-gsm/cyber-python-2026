# the pop() method 
# will always remove the last item but the set is unordered, we can't determine which 
# element will be popped from set
Months = ["January","February", "March", "April", "May", "June"]

for i in Months:
 
 Months.pop()
 print(Months)
print("\nPrinting the modified set...")
