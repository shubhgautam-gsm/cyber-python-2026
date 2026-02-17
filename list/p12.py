list1=[1,2,3,15,1,2,3,5,7,7]
list2=('ram','shyam','jay','rakesh')
print(list1)

list1.append(3)
print(list1)
newlist=list1.count(7)
print(newlist)
list1.extend([11,22,44,55])# extend multi append single
print(list1)
x=list1.index(15)
print(x)
list1.append([11,22])
print(list1)
list1.clear()
print(list1)



