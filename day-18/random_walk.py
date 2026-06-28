import turtle as t
import random

tim = t.Turtle()

# 1. Change color mode configuration to accept 24-bit RGB values
t.colormode(255)

def random_color():
    """Generates a truly random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# 2. Strict 90-degree cardinal angles (0=East, 90=North, 180=West, 270=South)
directions = [0, 90, 180, 270]

# 3. Make the line thicker and max out the turtle's animation speed
tim.pensize(15)
tim.speed("fastest")

# 4. Loop to keep the random path building over 200 steps
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
