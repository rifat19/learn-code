import turtle
import math
import time

# setup screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Triple Rotating Bars with Displacement")
turtle.tracer(0)  # turn off animation for smoother drawing

# create turtles
bar1 = turtle.Turtle()
bar2 = turtle.Turtle()
bar3 = turtle.Turtle()
path = turtle.Turtle()

for t in [bar1, bar2, bar3]:
    t.speed(0)
    t.pensize(4)
    t.hideturtle()

# setup trail-drawing turtle
path.speed(0)
path.color("red")
path.pensize(1)
path.penup()
path.hideturtle()

# constants
Length1 = 100  # length of first bar
Length2 = 60   # length of second bar
Length3 = 40   # length of third bar
angle_step = 2  # angle step for rotation
angle = 0  # initial angle of the first bar
displacement = 1  # displacement for the second and third bars
displaced_angle = 0  # angle for displacement

# Initial position for path
x1 = Length1 * math.cos(math.radians(angle))
y1 = Length1 * math.sin(math.radians(angle))
second_angle = angle * 6  # second bar rotates faster than first bar
x2 = x1 + Length2 * math.cos(math.radians(second_angle))
y2 = y1 + Length2 * math.sin(math.radians(second_angle))
third_angle = second_angle * 6  # third bar rotates faster than second bar
x3 = x2 + Length3 * math.cos(math.radians(third_angle))
y3 = y2 + Length3 * math.sin(math.radians(third_angle))
path.goto(x3, y3)  # move to the initial position of the third bar
path.pendown()  # start drawing the path

while True:
    bar1.clear()
    bar2.clear()
    bar3.clear()

    # First bar rotates from center
    x1 = Length1 * math.cos(math.radians(angle + displaced_angle))
    y1 = Length1 * math.sin(math.radians(angle + displaced_angle))
    bar1.penup()
    bar1.goto(0, 0)
    bar1.pendown()
    bar1.goto(x1, y1)

    # Second bar rotates around the endpoint of the first bar
    second_angle = angle * 6  # second bar rotates faster than first bar
    x2 = x1 + Length2 * math.cos(math.radians(second_angle + displaced_angle))
    y2 = y1 + Length2 * math.sin(math.radians(second_angle + displaced_angle))
    bar2.penup()
    bar2.goto(x1, y1)
    bar2.pendown()
    bar2.goto(x2, y2)

    # Third bar rotates around the endpoint of the second bar
    third_angle = second_angle * 6  # third bar rotates faster than second bar
    x3 = x2 + Length3 * math.cos(math.radians(third_angle + displaced_angle))
    y3 = y2 + Length3 * math.sin(math.radians(third_angle + displaced_angle))
    bar3.penup()
    bar3.goto(x2, y2)
    bar3.pendown()
    bar3.goto(x3, y3)

    # Apply displacement to the path turtle
    path.goto(x3, y3)  # move to the current position of the third bar

    # Apply displacement after every full 360° rotation
    if angle % 360 == 0:
        displaced_angle += displacement  # Increment displacement after each full rotation

    angle += angle_step  # increment angle
    if angle >= 360:
        angle -= 360  # reset angle to 0 after a full rotation

    turtle.update()  # update the screen
    time.sleep(0.01)  # add a small delay to control speed of animation
