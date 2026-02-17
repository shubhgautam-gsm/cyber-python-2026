# Using lambda with map function to square a list of numbers
numbers = [1, 2, 3, 4, 5]
numbers2 = [11, 22, 33, 44, 55]
squared_numbers = list(map(lambda i:i**2,numbers))





print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter function to filter out even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]



