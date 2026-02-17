# Assign values to a and b
a = 7  # binary: 0111
b = 3  # binary: 0010

     
# << left shift add zeros at right as give in b a<<b(3) 1011 =101100  
# >> left shift removes bits from right as give in b a>>b(3) =0001
 
# Perform left shift and right shift operations
left_shift = a << b  # Equivalent to moving bits of a to the left by 2 positions
right_shift = a >> b  # Equivalent to moving bits of a to the right by 2 positions

# Convert results to binary strings (for display purposes)
binary_left_shift = bin(left_shift)[2:].zfill(4)
binary_right_shift = bin(right_shift)[2:].zfill(4)

# Print results
print(f"a = {a} -> binary: {bin(a)[2:].zfill(4)}")
print(f"a << {b} = {left_shift} -> binary: {binary_left_shift}")
print(f"a >> {b} = {right_shift} -> binary: {binary_right_shift}")
