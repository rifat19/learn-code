import turtle
import time
import math

# Set up screen
screen = turtle.Screen()
screen.title("Analog Clock")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

# Draw clock face
face = turtle.Turtle()
face.hideturtle()
face.pensize(3)

def draw_clock_face():
    face.penup()
    face.goto(0, -250)
    face.pendown()
    face.circle(250)

    face.penup()
    face.goto(0, 0)
    face.setheading(90)

    for hour in range(12):
        face.forward(220)
        face.pendown()
        face.forward(20)
        face.penup()
        face.goto(0, 0)
        face.right(30)

draw_clock_face()

# Create clock hands
sec_hand = turtle.Turtle()
sec_hand.color("red")
sec_hand.pensize(1)
sec_hand.hideturtle()

min_hand = turtle.Turtle()
min_hand.color("blue")
min_hand.pensize(2)
min_hand.hideturtle()

hour_hand = turtle.Turtle()
hour_hand.color("black")
hour_hand.pensize(4)
hour_hand.hideturtle()

# Function to draw hands
def draw_hand(t, length, angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    t.right(angle)
    t.pendown()
    t.forward(length)

# Update the clock
def update_clock():
    while True:
        t = time.localtime()
        second = t.tm_sec
        minute = t.tm_min
        hour = t.tm_hour % 12

        # Clear previous hands
        sec_hand.clear()
        min_hand.clear()
        hour_hand.clear()

        # Draw hands
        draw_hand(hour_hand, 100, (hour + minute / 60) * 30)
        draw_hand(min_hand, 150, (minute + second / 60) * 6)
        draw_hand(sec_hand, 180, second * 6)

        screen.update()
        time.sleep(1)

update_clock()
