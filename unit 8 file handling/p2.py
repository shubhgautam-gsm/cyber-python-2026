# We should use the following method to overcome such type of problem.
try:
 fileptr = open("file1.txt","r")
 print(list(fileptr))
# perform file operations
finally:
 fileptr.close()
 print(list(fileptr))

