Employees = [(101, "Ayush", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
# 0 1 2 3
print(Employees,'\n')

print("----Printing list----")
for i in Employees:
 print(i)
 del Employees[1]

print("----Printing list after modification----")

for i in Employees:
 print(i)