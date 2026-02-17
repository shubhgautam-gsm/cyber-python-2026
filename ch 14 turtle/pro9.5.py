import turtle

def draw_eye(x, y, size, color):
    """Draws a single eye at the specified location."""
    eye = turtle.Turtle()
    eye.speed(0)
    eye.penup()
    eye.goto(x, y)
    eye.pendown()
    eye.fillcolor(color)
    eye.begin_fill()
    eye.circle(size)
    eye.end_fill()
    
    # Draw the pupil
    eye.penup()
    eye.goto(x, y - size / 2)
    eye.pendown()
    eye.fillcolor("black")
    eye.begin_fill()
    eye.circle(size / 4)
    eye.end_fill()

# Set up the screen
screen = turtle.Screen()
screen.setup(600, 400)
screen.bgcolor("white")

# Draw the eyes
draw_eye(-100, 50, 30, "blue")
draw_eye(100, 50, 30, "green")

# Hide the turtle
turtle.hideturtle()

turtle.done()