# Creating a set which have immutable elements
set1 = {1,2,3, "JavaTpoint", 20.5, 14}
print(type(set1))
#Creating a set which have mutable element
# set2 = {["Javatpoint",4],["Javatpoint2",5]}
# set2 = {("Javatpoint",4),("Javatpoint2",5)}
set2 = {("Javatpoint",(4,12,20)),("Javatpoint2",5)}
print(type(set2))   
print(dict(set2))