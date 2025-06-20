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
        screen.bgcolor("lightblue")  # Day
    else:
        screen.bgcolor("midnightblue")  # Night

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

# Create clock hand turtles
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

for hand, color, width in zip([hour_hand, minute_hand, second_hand], ['black', 'blue', 'red'], [6, 4, 2]):
    hand.hideturtle()
    hand.color(color)
    hand.pensize(width)

# Trail pendulum lines
joint1 = turtle.Turtle()
joint2 = turtle.Turtle()
for joint in [joint1, joint2]:
    joint.hideturtle()
    joint.color("gray")
    joint.pensize(1)

# Digital clock and date
digital = turtle.Turtle()
digital.hideturtle()
digital.penup()
digital.color("black")
digital.goto(0, -370)

calendar = turtle.Turtle()
calendar.hideturtle()
calendar.penup()
calendar.color("darkgreen")
calendar.goto(0, -400)

def draw_pendulum_chain():
    joint1.clear()
    joint2.clear()

    # Time values
    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour

    # Angles
    angle_h = (hour % 24 + minute / 60) * 15
    angle_m = (minute + sec / 60) * 6
    angle_s = sec * 6

    # Triple bar coordinates
    origin = (0, 0)
    x1 = 180 * math.cos(math.radians(90 - angle_h))
    y1 = 180 * math.sin(math.radians(90 - angle_h))
    x2 = x1 + 150 * math.cos(math.radians(90 - angle_m))
    y2 = y1 + 150 * math.sin(math.radians(90 - angle_m))
    x3 = x2 + 130 * math.cos(math.radians(90 - angle_s))
    y3 = y2 + 130 * math.sin(math.radians(90 - angle_s))

    # Draw hour hand
    hour_hand.clear()
    hour_hand.penup()
    hour_hand.goto(origin)
    hour_hand.pendown()
    hour_hand.goto(x1, y1)

    # Draw minute hand
    minute_hand.clear()
    minute_hand.penup()
    minute_hand.goto(x1, y1)
    minute_hand.pendown()
    minute_hand.goto(x2, y2)

    # Draw second hand
    second_hand.clear()
    second_hand.penup()
    second_hand.goto(x2, y2)
    second_hand.pendown()
    second_hand.goto(x3, y3)

    # Pendulum joints (gray lines)
    joint1.penup()
    joint1.goto(origin)
    joint1.pendown()
    joint1.goto(x1, y1)

    joint2.penup()
    joint2.goto(x1, y1)
    joint2.pendown()
    joint2.goto(x2, y2)

    # Digital time & date
    digital.clear()
    calendar.clear()
    digital.write(time.strftime("%H:%M:%S", t), align="center", font=("Courier", 24, "bold"))
    calendar.write(time.strftime("%A, %d %B %Y", t), align="center", font=("Courier", 16, "italic"))

# Update function
def update_clock():
    while True:
        update_background()
        draw_pendulum_chain()
        screen.update()
        time.sleep(1)

update_clock()
