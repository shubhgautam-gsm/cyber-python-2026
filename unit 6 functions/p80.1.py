mobiles=[5000,6000,12000,55000,9000,33000]

# Using lambda with filter function to filter out even numbers from a list
mobiles_filter = list(filter(lambda x: x <= 9000, mobiles))
print(mobiles_filter)  # Output: [2, 4]



