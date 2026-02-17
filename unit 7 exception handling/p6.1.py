try:
    # 1. Open for writing using 'with' statement for automatic closing
    with open("file2.txt", "w") as fileptr:
        fileptr.write("Hi I am good")
    
    print("File written and closed.")

    # 2. Open the file separately for reading
    with open("file2.txt", "r") as fileptr:
        content = fileptr.read() # Read the content
        print(content)
    
    print("File read and closed.")

except Exception as e:
    print("Error:", e)

print("Program finished.")
