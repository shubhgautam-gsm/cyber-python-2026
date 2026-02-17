import turtle
import random  # Importing the random module

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()
pen.speed(0)  # Speed '0' is the fastest in turtle graphics
pen.color("Red")

for x in range(50):
    # 0-1  1/10  0.1  0.01 0.10
    move = (random.random()*20) + 200  # Generate a random float between 0.0 and 1.0, then multiply by 200
    pen.backward(move)
    pen.left(170)

turtle.done()
