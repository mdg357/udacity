import turtle

def draw_square(length, t):
    for x in range(0, 4):
        t.forward(length)
        t.right(90)       

def draw_circle_of_squares(degreesToRotate, length, t):
    t.right(degreesToRotate)
    draw_square(length, t)

# Declare a turtle and a screen
window = turtle.Screen()
window.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.speed(100)
t.pencolor("white")

lineLength = 100
numberOfSquares = 90
degreesOfRotation = 360 / numberOfSquares

for x in range(0, numberOfSquares):
    draw_circle_of_squares(degreesOfRotation, lineLength, t)

window.exitonclick()
