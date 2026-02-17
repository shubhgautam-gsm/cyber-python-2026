# First, print the descending part -1 means detuct from 5
# 5-1 =4  4-1=3 ... until 1   if (5,0,-2) 5-2=3 until 1
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    for j in range(1,6-i):
        print(j, end=' ')
       
    print('\n')

# Then, print the ascending part
