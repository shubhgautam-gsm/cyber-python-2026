# Unlike lists, the tuple items can not be deleted by using the del keyword as tuples are
# immutable. To delete an entire tuple, we can use the del keyword with the tuple
# name.

# tuple1= [1, 2, 3, 4, 5, 6]  #list
tuple1= (1, 2, 3, 4, 5, 6) #tuples are immutable
print(tuple1)
# del tuple1[0:4]
print(tuple1)
# del tuple1
print(tuple1)