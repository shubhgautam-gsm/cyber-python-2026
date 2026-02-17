import turtle


turtle.Screen().setup(width=600, height=400)
pen = turtle.Turtle()

pen.color("red")

angles = [10, 40, 90]

for angle in angles:
    # setheading gives angle from X-axis 
    # left() or right() gives angle from current position 
    pen.setheading(angle)
    pen.backward(200)

pen.left(144)
turtle.done()
