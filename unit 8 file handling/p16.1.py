#open the file.txt in read mode. causes error if no such file exists
try:
 fileptr = open("7.txt","x")    
 print(fileptr)
except Exception as e:
 print('file already exist')
else:
 print("File created successfully")
