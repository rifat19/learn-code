import turtle
import time
import math

# Setup screen
screen = turtle.Screen()
screen.title("Triple Pendulum Hybrid Clock")
screen.setup(width=1000, height=1000)
screen.tracer(0)

# Clock face (fixed hour dial)
face = turtle.Turtle()
face.hideturtle()
face.pensize(3)

def draw_main_face():
    face.clear()
    face.penup()
    face.goto(0, -200)
    face.pendown()
    face.circle(200)
    
    face.penup()
    face.goto(0, 0)
    face.setheading(90)

    for _ in range(24):
        face.forward(180)
        face.pendown()
        face.forward(20)
        face.penup()
        face.goto(0, 0)
        face.right(15)

draw_main_face()

# Create turtles for hands
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

for hand, color, width in zip([hour_hand, minute_hand, second_hand], ['black', 'blue', 'red'], [6, 4, 2]):
    hand.hideturtle()
    hand.color(color)
    hand.pensize(width)

# Joints
joint1 = turtle.Turtle()
joint2 = turtle.Turtle()
for joint in [joint1, joint2]:
    joint.hideturtle()
    joint.color("gray")
    joint.pensize(1)

# Display circles
minute_circle = turtle.Turtle()
second_circle = turtle.Turtle()

minute_circle.hideturtle()
minute_circle.pensize(2)
minute_circle.color("blue")

second_circle.hideturtle()
second_circle.pensize(2)
second_circle.color("red")

# Time display text
digital = turtle.Turtle()
calendar = turtle.Turtle()
for disp in [digital, calendar]:
    disp.hideturtle()
    disp.penup()

digital.goto(0, -420)
calendar.goto(0, -450)

def draw_analog_circle(turtle_obj, center_x, center_y, radius, divisions):
    turtle_obj.clear()
    turtle_obj.penup()
    turtle_obj.goto(center_x, center_y - radius)
    turtle_obj.setheading(0)
    turtle_obj.pendown()
    turtle_obj.circle(radius)

    turtle_obj.penup()
    for i in range(divisions):
        angle = math.radians(90 - (360 / divisions) * i)
        x1 = center_x + (radius - 20) * math.cos(angle)
        y1 = center_y + (radius - 20) * math.sin(angle)
        x2 = center_x + radius * math.cos(angle)
        y2 = center_y + radius * math.sin(angle)
        turtle_obj.goto(x1, y1)
        turtle_obj.pendown()
        turtle_obj.goto(x2, y2)
        turtle_obj.penup()

def draw_pendulum_clock():
    # Clear hands
    hour_hand.clear()
    minute_hand.clear()
    second_hand.clear()
    joint1.clear()
    joint2.clear()
    digital.clear()
    calendar.clear()
    angle_display.clear()

    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour

    # Angles
    angle_h = (hour % 24 + minute / 60) * 15
    angle_m = (minute + sec / 60) * 6
    angle_s = sec * 6

    origin = (0, 0)
    x1 = 170 * math.cos(math.radians(90 - angle_h))
    y1 = 170 * math.sin(math.radians(90 - angle_h))
    x2 = x1 + 120 * math.cos(math.radians(90 - angle_m))
    y2 = y1 + 120 * math.sin(math.radians(90 - angle_m))
    x3 = x2 + 100 * math.cos(math.radians(90 - angle_s))
    y3 = y2 + 100 * math.sin(math.radians(90 - angle_s))

    # Draw hands
    hour_hand.penup()
    hour_hand.goto(origin)
    hour_hand.pendown()
    hour_hand.goto(x1, y1)

    minute_hand.penup()
    minute_hand.goto(x1, y1)
    minute_hand.pendown()
    minute_hand.goto(x2, y2)

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

    # Moving analog circles
    draw_analog_circle(minute_circle, x1, y1, 160, 1)
    draw_analog_circle(second_circle, x2, y2, 140, 1)

    # Center digital clock
    digital.write(time.strftime("%H:%M:%S", t), align="center", font=("Courier", 24, "bold"))

    angle_display.write(
        f"{angle_h:.2f}°  :  {angle_m:.2f}°  :  {angle_s:.2f}°",
        align="center",
        font=("Courier", 14, "normal")
    )

    calendar.write(time.strftime("%A, %d %B %Y", t), align="center", font=("Courier", 16, "italic"))

   # angle_display.write(
   #     f"Hour: {angle_h:.2f}°  |  Minute: {angle_m:.2f}°  |  Second: {angle_s:.2f}°",
   #     align="center",
   #     font=("Courier", 14, "normal")
   # )


angle_display = turtle.Turtle()
angle_display.hideturtle()
angle_display.penup()
angle_display.goto(0, -480)

def update_loop():
    while True:
        draw_pendulum_clock()
        screen.update()
        time.sleep(1)

update_loop()
