from turtle import Turtle, Screen

tim = Turtle()

# Loop 4 times to draw 4 sides
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
