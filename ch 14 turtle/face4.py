import turtle
import random

# Initialize screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=800)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Helper functions for drawing
def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_face_shape():
    skin_color = (1, 0.87, 0.77)
    turtle.colormode(1.0)
    t.fillcolor(skin_color)
    move_to(t, -70, -100)
    t.begin_fill()
    t.setheading(0)
    t.circle(100)  # Changed from rectangle to oval shape for a more realistic face
    t.end_fill()

# Draw hair with random style
def draw_hair():
    hair_colors = [(0.4, 0.2, 0.1), (0, 0, 0), (1, 0.85, 0.35), (0.8, 0.2, 0.2)]
    hair_color = random.choice(hair_colors)
    t.fillcolor(hair_color)
    move_to(t, -90, 80)
    t.begin_fill()
    t.setheading(60)
    for _ in range(20):  # Increased loop for fuller hair
        t.forward(15)
        t.right(9)
    t.end_fill()

# Draw eyes
def draw_eyes():
    eye_colors = [(0, 0, 1), (0, 0.5, 0), (0.4, 0.2, 0.1), (0.5, 0.4, 0.3)]
    eye_color = random.choice(eye_colors)
    pupil_color = (0, 0, 0)
    
    for x in [-30, 30]:  # Simplified eye drawing loop for both eyes
        move_to(t, x, 20)
        t.fillcolor("white")
        t.begin_fill()
        t.circle(15)
        t.end_fill()

        move_to(t, x, 25)
        t.fillcolor(eye_color)
        t.begin_fill()
        t.circle(7)
        t.end_fill()

        move_to(t, x, 28)
        t.fillcolor(pupil_color)
        t.begin_fill()
        t.circle(3)
        t.end_fill()

# Draw nose
def draw_nose():
    move_to(t, 0, 5)
    t.setheading(-90)
    t.pensize(2)
    t.pendown()
    t.circle(5, 180)
    t.pensize(1)
    t.penup()

# Draw mouth
def draw_mouth():
    lip_colors = [(1, 0.4, 0.6), (0.9, 0, 0)]
    lip_color = random.choice(lip_colors)
    
    move_to(t, -30, -40)
    t.fillcolor(lip_color)
    t.begin_fill()
    t.setheading(-60)
    t.circle(30, 120)
    t.setheading(180)
    t.circle(30, 120)
    t.end_fill()

# Draw eyebrows
def draw_eyebrows():
    t.pensize(4)
    eyebrow_color = (0, 0, 0)
    t.pencolor(eyebrow_color)

    for x, angle in [(-40, 20), (20, 160)]:  # Simplified eyebrow loop
        move_to(t, x, 50)
        t.setheading(angle)
        t.forward(40)

    t.pensize(1)

# Main function to draw the face
def generate_random_realistic_face():
    draw_face_shape()
    draw_hair()
    draw_eyes()
    draw_nose()
    draw_mouth()
    draw_eyebrows()
    
    screen.exitonclick()

# Generate the face
generate_random_realistic_face()
