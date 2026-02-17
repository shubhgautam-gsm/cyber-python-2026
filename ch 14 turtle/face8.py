import turtle as t
import random

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_face():
    t.speed(2)
    t.hideturtle()
    t.bgcolor("white")
    
    # Face color
    face_color = (random.random(), random.random(), random.random())
    t.fillcolor(face_color)
    
    # Draw face
    move_to(0, -50)
    t.begin_fill()
    t.setheading(0)
    t.forward(60)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(60)
    t.end_fill()

    # Draw left eye
    eye_color = (random.random(), random.random(), random.random())
    move_to(-30, 25)
    t.fillcolor(eye_color)
    t.begin_fill()
    t.setheading(0)
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.end_fill()

    # Draw right eye
    move_to(20, 25)
    t.begin_fill()
    t.setheading(0)
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(5)
    t.end_fill()

    # Draw left pupil
    pupil_color = (random.random(), random.random(), random.random())
    move_to(-27, 27)
    t.fillcolor(pupil_color)
    t.begin_fill()
    t.setheading(0)
    t.forward(5)
    t.left(90)
    t.forward(3)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(3)
    t.end_fill()

    # Draw right pupil
    move_to(23, 27)
    t.begin_fill()
    t.setheading(0)
    t.forward(5)
    t.left(90)
    t.forward(3)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(3)
    t.end_fill()

    # Draw mouth
    mouth_color = (random.random(), random.random(), random.random())
    move_to(-20, -20)
    t.fillcolor(mouth_color)
    t.begin_fill()
    t.setheading(0)
    t.forward(40)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(5)
    t.end_fill()

    # Draw nose
    move_to(-5, 5)
    t.setheading(-90)
    t.forward(15)
    t.right(135)
    t.forward(10)
    t.penup()
    t.goto(0, 5)
    t.pendown()
    t.setheading(-90)
    t.forward(15)
    t.right(45)
    t.forward(10)

draw_face()
t.done()
