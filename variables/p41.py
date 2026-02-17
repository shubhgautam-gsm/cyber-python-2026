# stone
# paper
# scissor

# Function to check the winner
player1 = str(input("Enter Choose One Stone|Paper|Scissor ? ")).upper()
player2 = str(input("Enter Choose One Stone|Paper|Scissor ? ")).upper()

if player1=='Stone' and player2=='Paper':
 print("PLAYER 2 IS WINNER") 
if player1=='Scissor' and player2=='Paper':
 print("PLAYER 1 IS WINNER")
if player1=='STONE' and player2=='SCISSOR':
 print("PLAYER 2 IS WINNER")
if player1=='Stone' and player2=='Stone' | player1=='Scissor' and player2=='Scissor'| player1=='Paper' and player2=='Paper':
 print("ITS A DRAW")