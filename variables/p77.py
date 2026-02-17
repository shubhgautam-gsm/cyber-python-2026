n=3
while 1:
 i=1
 while i<=10:
     print("%d X %d = %d\n"%(n,i,n*i))
     i = i+1
 
 choice = int(input("Do you want to continue printing the table any number except 0 to continue?"))
 if choice == 0:
     break
 n=n+1