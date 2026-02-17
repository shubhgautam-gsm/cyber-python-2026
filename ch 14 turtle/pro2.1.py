import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()
for x in range(1, 45):
   
    move=float(input('write move value:'))
    pen.forward(move)
   
    direct=float(input('write direction value:')) 
    pen.left(direct)
    space='\n\n '
    
pen.left(90)    
turtle.done()

