# This type of arguments is useful when we do not know the number of arguments inadvance.
# It is similar as the *args but it stores the argument in the dictionary format.
def food(**any):
 print(any)
 
food(fruit=["Apple","mango"],veg=['cabbage','palak'])
# food(fruits="Orange", Vagitables="Carrot")
# {'a': 'Apple'}
# {'fruits': 'Orange', 'Vagitables': 'Carrot'}
