import turtle as t
import random

tim = t.Turtle()
t.colormode(255)  # Allows us to use random RGB colors
tim.speed("fastest")  # Speeds up the drawing animation drastically


def random_color():
    """Generates a random RGB color tuple."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    """Draws a series of circles offset by a specific angle gap."""
    # 360 degrees divided by the gap size gives the exact number of loops needed
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)  # Draws a circle with a radius of 100 pixels

        # Shift the orientation slightly before drawing the next circle
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


# Run the spirograph function with a 5-degree shift gap
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
