import turtle

# Setup screen and pen
turtle.Screen().setup(width=600, height=400)
pen = turtle.Turtle()
pen.color("red")
pen.speed(0)  # Maximize drawing speed for complexity

# Define angles dynamically for smoother, more organic patterns
angles = [15, 25, 30, 40, 55, 75, 85, 100, 120, 135, 155, 170, 190, 220, 240, 270, 300, 330, 360]

# Draw intricate pattern with dynamic forward and backward movements
for angle in angles:
    pen.setheading(angle)
    pen.forward(3)  # Slight forward movement to create detailed design
    pen.backward(3)  # Move back to create the intricate design

    # Creating "leaf-like" eyes shape dynamically (based on angle)
    if angle == 90:  # Left leaf-like eye
        pen.penup()
        pen.goto(-50, 50)  # Position for the left eye
        pen.pendown()
        pen.setheading(45)  # Start angle for a leaf shape
        pen.circle(20, 90)  # Draw the top curve of the leaf (quarter-circle)
        pen.setheading(225)  # Change heading to make bottom curve
        pen.circle(20, 90)  # Draw the bottom curve of the leaf (quarter-circle)
        
    if angle == 270:  # Right leaf-like eye
        pen.penup()
        pen.goto(50, 50)  # Position for the right eye
        pen.pendown()
        pen.setheading(135)  # Start angle for a leaf shape
        pen.circle(20, 90)  # Draw the top curve of the leaf (quarter-circle)
        pen.setheading(315)  # Change heading to make bottom curve
        pen.circle(20, 90)  # Draw the bottom curve of the leaf (quarter-circle)

# Hide the pen and display the result
pen.hideturtle()
turtle.done()
