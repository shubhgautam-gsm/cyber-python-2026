a = [1, 2, 3]
b = a
c = [1, 2, 3]

# a and b point to the same object
print('a ej b che ?',a is b)
print('a  b na barobar che ?',a == b)
print('a ej c che ?',a is c)  # False
print('a  c na barobar che ?',a == c)  # True
print(a is not b) # False
# a and c do not point to the same object, even though they have the same cont
