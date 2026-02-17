def farToCel(f):
 c=5/9*(f-32)
 return f"{round(c, 2)}°C"
#  return round(c,2)
# .2f  f{}



far = (84, 72, 93, 84)
print(f"Fahrenheit values: {tuple(f'{f}F°' for f in far)}")


result = map(farToCel, far)
# print(result)
# converting map object to set
# numbersAddition = set(result)

numbersAddition = tuple(result)
print("Celsius values:",numbersAddition)