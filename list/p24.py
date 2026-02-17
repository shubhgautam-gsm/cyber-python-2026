# Creating a set which have immutable elements
set1 = {1,2,3, "JavaTpoint", 20.5, 14}
print(type(set1))
#Creating a set which have mutable element
# set2 = {1,2,3,("Javatpoint",4)}
set2 = {1,2,3,["Javatpoint",4]} # not accept mutable i.e list
print(type(set2))   
print(set2)   