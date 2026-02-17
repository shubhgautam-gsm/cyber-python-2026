# open the file file1.txt in read mode
fileptr = open("file2.txt","r")

#-work same but read load uncessary data
#-work same but seek not load unccessary data but jump pointer to that part
print("The filepointer is at byte :",fileptr.seek(12))
 #before using read() our pointer at first(0)  position
# but seek (10) will move pointer to 10th position
print("The filepointer is at byte :",fileptr.read())
print("The filepointer is at byte :",fileptr.tell())

fileptr.read() #after using read() our pointer at last position
# print("The filepointer is at byte :",)


print("The filepointer is at byte :",fileptr.tell())

