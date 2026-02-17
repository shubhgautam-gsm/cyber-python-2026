import turtle
import math

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Scaling factor (adjust to change overall size)
scale = 3

# Define the points that roughly outline the eye shape (adjust these)
eye_points = [
    (-7 * scale, 0),
    (-6 * scale, 4 * scale),
    (-4 * scale, 7 * scale),
    (-1 * scale, 8 * scale),
    (2 * scale, 7 * scale),
    (5 * scale, 5 * scale),
    (7 * scale, 0),
    (5 * scale, -5 * scale),
    (2 * scale, -7 * scale),
    (-1 * scale, -8 * scale),
    (-4 * scale, -7 * scale),
    (-6 * scale, -4 * scale),

]

# Move to the starting point
pen.penup()
pen.goto(eye_points[0])
pen.pendown()

# Draw the outline
pen.pensize(2)
pen.color("black")

for point in eye_points:
    pen.goto(point)

# Draw the pupil (inner circle)
pen.penup()

# Approximate center of the eye (adjust if needed)
center_x = -2 * scale
center_y = -1 * scale
pupil_radius = 2 * scale

pen.goto(center_x, center_y - pupil_radius) # Start below the circle
pen.pendown()

pen.fillcolor("black")
pen.begin_fill()
pen.circle(pupil_radius)
pen.end_fill()


turtle.done()