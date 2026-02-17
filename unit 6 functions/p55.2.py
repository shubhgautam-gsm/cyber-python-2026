# Python filter() function example
# x ='apple' 0
# x ='angur' 1
# x = 'banana' 2 if condi true
fruits_list=('apple','angur','banana','berry')

user=input('search fruits type words:')
def filterdata(x):
  #  if user in x: in 'a' word in laptop
 if user in x[0]:
  return x
# Calling function

result= filter(filterdata,fruits_list)
# Displaying result
print(list(result))
  