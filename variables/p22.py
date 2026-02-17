jaydeep=int(input('Enter marks:'))
passs=40

if jaydeep >= passs and jaydeep <=100:
    print('Pass because you  have marks ',jaydeep)
elif jaydeep >= 100 or jaydeep < 0:
    print('marks is invalid ',jaydeep)
else:
    print('Fail because you  have marks ',jaydeep)