f = open("file1.txt", 'r')



# Now attempting to perform file operations
try:
   try:  
     a=5
     b=6
     c=a+d # line break / exit
   finally:
     f.close()
 
except Exception as e:
    print("The file is closed.")

content = f.read()
print(content)