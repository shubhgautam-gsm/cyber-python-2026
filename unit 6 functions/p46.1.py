# Creating a bytearray
original_data = bytearray(b'Hello, world!')

# Using memory views
mv = original_data
print("Memory view example:")
print(mv[0:5]) 



# Using traditional slicing (copying data)
copied_data = original_data[0:5]
print("\nTraditional slicing example:")
print(copied_data)  # Printing the copied data