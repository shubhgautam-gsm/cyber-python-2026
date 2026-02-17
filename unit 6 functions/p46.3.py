original_data = bytearray(b"Hello, world!")

# --- Using memoryview (no copy) ---
mv = memoryview(original_data)
print("Memory view before change:", bytes(mv[:5]))

# Modify through memoryview
mv[0:5] = b"YELLO"  
print("After modifying memoryview:")
print("original_data ->", original_data)
print("memoryview    ->", bytes(mv[:5]))