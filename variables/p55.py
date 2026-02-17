# First, print the descending part -1 means detuct from 5
# 5-1 =4  4-1=3 ... until 1   if (5,0,-2) 5-2=3 until 1
# Then, print the ascending part
# over
# imp
# MAIN LOOP FOR (PARENT) HOW MANY ROWS WANT TO PRINT 3
# 0 1 2 3 4 ROW 1
# 0 1 2 3 4 ROW 2
# 0 1 2 3 4 ROW 3
# THEN CHILD LOOP FOR VALUE PRINT UNTIL STARTING TO ENDING
# 0 1 2 3 4 
# N3..N4 
for i in range(0, 4): # increment 0 - 1 - 2 ... 4
    
    for j in range(5,i,-1): # decrement 5 -4 - 3 ... 5
     print(j, end=' ')  #1 2 3 4 

    for j in range(1,i+1): # decrement 5 -4 - 3 ... 5
     print(j, end=' ')  #1 2 3 4 

    print('\n')

