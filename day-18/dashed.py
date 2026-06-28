from turtle import Turtle, Screen

tim = Turtle()

# Alternate between drawing and moving forward blankly
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
