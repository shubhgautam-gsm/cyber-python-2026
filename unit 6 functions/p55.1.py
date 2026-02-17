# Python filter() function example
# x = ('apple','banana','berry')
def filterdata(x):
 if 'a'in x[0]:
  return x
# Calling function

user=input('choose for filter a or b')
if(user=='a'):
    result= filter(filterdata,('apple','banana','berry'))
elif(user=='b'):
    result= filter(filterdata,('apple','banana','berry'))

# Displaying result
print(list(result))
  