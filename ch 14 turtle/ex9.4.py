import turtle
# Setup
screen = turtle.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("white")

t = turtle.Turtle() #pencil 1


t.speed(2)
t.color("yellow")
t.width(27)
t.circle(100,-60)

t.color("red")
t.circle(100,-80)


t.color("green")







# Hide the turtle
t.hideturtle()

# Keep window open
screen.mainloop()
