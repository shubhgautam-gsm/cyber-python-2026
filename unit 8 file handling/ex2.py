def process_file(filename):
    try:
        fileptr = open(filename, "r")
        
        if fileptr:
                print("File is opened successfully")
                file_content = fileptr.read()
                print("Content of", filename, ":")
                print(file_content)
                1 / 0   # Simulate error 
                fileptr.close()   # <-- will never run if error occurs above
    
    
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred during processing:", str(e))

    print(file_content)
    
    
process_file("file2.txt")
