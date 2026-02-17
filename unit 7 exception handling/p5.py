try:
#  a=10/0
#  a=int(input('Enter a number'))
 fileptr = open("fil2.txt","r")
except(IOError):
 print("File Naming Exception")
else:
 print("Successfully Done")



# try:
#  a=10/0
# #  a=int(input('Enter a number'))
# #  fileptr = open("fil2.txt","r")
# except Exception as e:
#  print(e)
# else:
#  print("Successfully Done")
