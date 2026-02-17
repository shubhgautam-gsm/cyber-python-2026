import turtle
import random

def draw_circle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)  # Adjust to start from the top of the circle
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_ellipse(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    
    # Draw an ellipse by stretching the circle
    t.setheading(0)
    for i in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
        
    t.end_fill()

def generate_random_face():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=600, height=600)
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Random face parameters
    face_radius = random.randint(100, 150)
    eye_radius = random.randint(10, 20)
    eye_y_offset = random.randint(20, 40)
    eye_x_offset = random.randint(30, 50)
    mouth_width = random.randint(50, 80)
    mouth_height = random.randint(20, 30)

    # Random colors
    face_color = (random.random(), random.random(), random.random())
    eye_color = (random.random(), random.random(), random.random())
    mouth_color = (random.random(), random.random(), random.random())

    # Convert to turtle color mode (0-255)
    turtle.colormode(1.0)

    # Draw face
    draw_circle(t, 0, 0, face_radius, face_color)

    # Draw left eye
    draw_circle(t, -eye_x_offset, eye_y_offset, eye_radius, eye_color)

    # Draw right eye
    draw_circle(t, eye_x_offset, eye_y_offset, eye_radius, eye_color)

    # Draw mouth (ellipse)
    t.penup()
    t.goto(0, -face_radius + 50)
    t.setheading(0)
    t.pendown()
    t.fillcolor(mouth_color)
    t.begin_fill()
    
    for _ in range(2):
        t.circle(mouth_width, 90)
        t.circle(mouth_height, 90)
    
    t.end_fill()

    # Keep the window open until clicked
    

# Run the function to generate a random face
generate_random_face()
