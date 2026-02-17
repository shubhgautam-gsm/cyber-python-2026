with open("file1.txt", 'r') as f:
    content = f.read()
    print(content) 
    # locally perform

# Attempting to perform file operations outside the `with` block
try:
    f.read()
except ValueError:
    print("The file is closed.")
else:
    print("The file is still open.")
