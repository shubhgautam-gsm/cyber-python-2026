# Assign values to a and b
a = 7
b = 6

# Convert a and b to binary strings (for display purposes)
binary_a = bin(a)[2:].zfill(4)
binary_b = bin(b)[2:].zfill(4)

# Perform bitwise operations
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not_a = ~a & 0b1111  # Using 0b1111 to limit the result to 4 bits

# Convert results to binary strings (for display purposes)
binary_and = bin(bitwise_and)[2:].zfill(4)
binary_or = bin(bitwise_or)[2:].zfill(4)
binary_xor = bin(bitwise_xor)[2:].zfill(4)
binary_not_a = bin(bitwise_not_a)[2:].zfill(4)

# Print results
print(f"a = {a} -> binary: {binary_a}")
print(f"b = {b} -> binary: {binary_b}")
print(f"a & b = {bitwise_and} -> binary: {binary_and}")
print(f"a | b = {bitwise_or} -> binary: {binary_or}")
print(f"a ^ b = {bitwise_xor} -> binary: {binary_xor}")
print(f"~a = {bitwise_not_a} -> binary: {binary_not_a}")
