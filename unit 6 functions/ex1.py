def farToCel(f):
 return f[0]*f[1]
  
f=[4,2]  
  
far = ([4, 2], [93, 84])
result = map(farToCel, far)
numbersAddition = tuple(result)
print("Celsius values:",numbersAddition)