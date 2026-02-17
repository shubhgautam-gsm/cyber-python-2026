
for i in range(0, 5): # increment 0 - 1 - 2 ... 4
    
    for j in range(5,i,-1): # decrement 5 -4 - 3 ... 5
     print("*", end=' ')  #1 2 3 4 

    for j in range(0,i+1): # decrement 5 -4 - 3 ... 5
     print(" ", end=' ')  #1 2 3 4 
    
    for j in range(1,i+1): # decrement 5 -4 - 3 ... 5
     print(" ", end=' ')  #1 2 3 4 
    
    for j in range(5,i,-1): # decrement 5 -4 - 3 ... 5
     print("*", end=' ')  #1 2 3 4 

    
    print('\n')
    
for i in range(5, 0,-1): # increment 0 - 1 - 2 ... 4
    # for j in range(i,6): # decrement 5 -4 - 3 ... 5
    #  print(" ", end=' ')  #1 2 3 4  
    for j in range(6,i,-1): # decrement 5 -4 - 3 ... 5
     print("*", end=' ')  #1 2 3 4 

    for j in range(1,i): # decrement 5 -4 - 3 ... 5
     print(" ", end=' ')  #1 2 3 4 
    
    for j in range(0,i): # decrement 5 -4 - 3 ... 5
     print(" ", end=' ')  #1 2 3 4 
    
    for j in range(6,i,-1): # decrement 5 -4 - 3 ... 5
     print("*", end=' ')  #1 2 3 4 
    print('\n')

