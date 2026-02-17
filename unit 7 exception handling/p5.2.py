try:

 fileptr = open("file2.txt","r")

except Exception as e:
 print('FOR FILE ',e) # BY GIVING WARNING

else:
 print("Successfully Done")
