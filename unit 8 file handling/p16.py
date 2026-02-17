#open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file6.txt","x")
#  'x' for file create

print(fileptr)
if fileptr:
 print("File created successfully")
