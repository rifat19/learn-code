import turtle
import time
import math

# Setup screen
screen = turtle.Screen()
screen.title("Triple Pendulum Hybrid Clock")
screen.setup(width=800, height=800)
screen.tracer(0)

# Colors for day and night
def update_background():
    current_hour = time.localtime().tm_hour
    if 6 <= current_hour < 18:
        screen.bgcolor("lightblue")
    else:
        screen.bgcolor("midnightblue")

# Draw clock face
face = turtle.Turtle()
face.hideturtle()
face.pensize(3)

def draw_face():
    face.penup()
    face.goto(0, -300)
    face.pendown()
    face.circle(300)
    
    face.penup()
    face.goto(0, 0)
    face.setheading(90)

    for _ in range(12):
        face.forward(270)
        face.pendown()
        face.forward(20)
        face.penup()
        face.goto(0, 0)
        face.right(30)

draw_face()

# Clock hand turtles
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()
for hand, color, width in zip([hour_hand, minute_hand, second_hand], ['black', 'blue', 'red'], [6, 4, 2]):
    hand.hideturtle()
    hand.pensize(width)
    hand.color(color)

# Pendulum joints
joint1 = turtle.Turtle()
joint2 = turtle.Turtle()
for joint in [joint1, joint2]:
    joint.hideturtle()
    joint.color("gray")
    joint.pensize(1)

# Center digital clock and calendar
digital = turtle.Turtle()
calendar = turtle.Turtle()
for t in [digital, calendar]:
    t.hideturtle()
    t.penup()
digital.color("black")
digital.goto(0, -370)
calendar.color("darkgreen")
calendar.goto(0, -400)

# Create moving digital time labels
label_hour = turtle.Turtle()
label_minute = turtle.Turtle()
label_second = turtle.Turtle()
for label in [label_hour, label_minute, label_second]:
    label.hideturtle()
    label.penup()
    label.color("black")

# Drawing everything
def draw_pendulum_chain():
    joint1.clear()
    joint2.clear()
    label_hour.clear()
    label_minute.clear()
    label_second.clear()
    digital.clear()
    calendar.clear()

    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour

    angle_h = (hour % 24 + minute / 60) * 15
    angle_m = (minute + sec / 60) * 6
    angle_s = sec * 6

    origin = (0, 0)
    x1 = 100 * math.cos(math.radians(90 - angle_h))
    y1 = 100 * math.sin(math.radians(90 - angle_h))
    x2 = x1 + 100 * math.cos(math.radians(90 - angle_m))
    y2 = y1 + 100 * math.sin(math.radians(90 - angle_m))
    x3 = x2 + 100 * math.cos(math.radians(90 - angle_s))
    y3 = y2 + 100 * math.sin(math.radians(90 - angle_s))

    # Draw hands
    hour_hand.clear()
    hour_hand.penup()
    hour_hand.goto(origin)
    hour_hand.pendown()
    hour_hand.goto(x1, y1)

    minute_hand.clear()
    minute_hand.penup()
    minute_hand.goto(x1, y1)
    minute_hand.pendown()
    minute_hand.goto(x2, y2)

    second_hand.clear()
    second_hand.penup()
    second_hand.goto(x2, y2)
    second_hand.pendown()
    second_hand.goto(x3, y3)

    # Draw joints
    joint1.penup()
    joint1.goto(origin)
    joint1.pendown()
    joint1.goto(x1, y1)

    joint2.penup()
    joint2.goto(x1, y1)
    joint2.pendown()
    joint2.goto(x2, y2)

    # Draw digital labels
    label_hour.goto(x1 + 15, y1 + 15)
    label_hour.write(f"{hour:02}", align="center", font=("Arial", 10, "bold"))

    label_minute.goto(x2 + 15, y2 + 15)
    label_minute.write(f"{minute:02}", align="center", font=("Arial", 10, "bold"))

    label_second.goto(x3 + 15, y3 + 15)
    label_second.write(f"{sec:02}", align="center", font=("Arial", 10, "bold"))

    # Center digital time and calendar
    digital.write(time.strftime("%H:%M:%S", t), align="center", font=("Courier", 24, "bold"))
    calendar.write(time.strftime("%A, %d %B %Y", t), align="center", font=("Courier", 16, "italic"))

# Keep updating every second
def update():
    update_background()
    draw_pendulum_chain()
    screen.update()
    screen.ontimer(update, 1000)

update()
turtle.done()
