# Original data
original_data = bytearray(b"Hello, world!")



# --- Using slicing (copy) ---
copied_data = original_data[0:5]
print("\nSlicing before change:", copied_data)

# Modify copied_data
copied_data[0] = 88  # 'X'
print("After modifying slice copy:")
print("original_data ->", original_data)
print("copied_data   ->", copied_data)

