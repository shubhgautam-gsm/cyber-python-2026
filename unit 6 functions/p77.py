numList = [44, 55, 66] #=[],(),{} #keys
strList = ['four', 'five', 'six'] #values

result = zip(numList, strList) #zip() function joint two list then need to convert it into dict {key:value}
resultSet = dict(result)
print(resultSet)
