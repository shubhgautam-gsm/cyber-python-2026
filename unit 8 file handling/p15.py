# print single line
#open the file.txt in read mode. causes error if no such file exists.
fileptr = open("file2.txt","r")
#stores all the data of the file into the variable content
content = fileptr.readline(2)
content1 = fileptr.readline()
content2 = fileptr.readline()
content3 = fileptr.readline()
print(content) #prints the content of the file
print(content1)
print(content2)
print(content3)
fileptr.close() #closes the opened file