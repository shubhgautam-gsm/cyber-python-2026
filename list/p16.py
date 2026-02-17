# tuple1 = list(input("Enter the tuple elements ..."))
# tuple1 = set(input("Enter the tuple elements ..."))
tuple1 = tuple(input("Enter the tuple elements ..."))
print(tuple1)
count = 0
for i in tuple1:
 print("tuple1[%d] = %s"%(count, i))