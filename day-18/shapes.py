import random
from turtle import Turtle, Screen

tim = Turtle()

# List of distinct colors for the shapes
colors = ["cornflower blue", "dark orchid", "indian red", "deep sky blue", "light sea green", "slate gray", "sea green"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# Outer loop sets the range of sides (3 to 10)
for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
