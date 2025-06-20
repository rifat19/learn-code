import pygame
import tkinter as tk
import time
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hybrid Clock (Analog-Digital with Triple Pendulum)")

# Colors
DAY_COLOR = (200, 230, 255)
NIGHT_COLOR = (20, 20, 70)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Font for digital clock
pygame.font.init()
font_digital = pygame.font.SysFont("Courier", 36)
font_date = pygame.font.SysFont("Courier", 24)

# Tkinter setup for date
root = tk.Tk()
root.withdraw()  # hide the main window

# Helper function to get background color
def get_background_color():
    hour = time.localtime().tm_hour
    return DAY_COLOR if 6 <= hour < 18 else NIGHT_COLOR

# Draw analog clock face
def draw_clock_face():
    pygame.draw.circle(screen, BLACK, CENTER, 300, 4)
    for i in range(12):
        angle = math.radians(i * 30)
        x_outer = CENTER[0] + int(280 * math.cos(angle - math.pi / 2))
        y_outer = CENTER[1] + int(280 * math.sin(angle - math.pi / 2))
        x_inner = CENTER[0] + int(260 * math.cos(angle - math.pi / 2))
        y_inner = CENTER[1] + int(260 * math.sin(angle - math.pi / 2))
        pygame.draw.line(screen, BLACK, (x_inner, y_inner), (x_outer, y_outer), 2)

# Convert angle to position
def get_pos(length, angle_deg, origin):
    angle_rad = math.radians(angle_deg - 90)
    x = origin[0] + length * math.cos(angle_rad)
    y = origin[1] + length * math.sin(angle_rad)
    return (x, y)

# Draw triple pendulum
def draw_pendulum_chain():
    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour

    angle_h = (hour % 24 + minute / 60) * 15
    angle_m = (minute + sec / 60) * 6
    angle_s = sec * 6

    x1, y1 = get_pos(100, angle_h, CENTER)
    x2, y2 = get_pos(100, angle_m, (x1, y1))
    x3, y3 = get_pos(100, angle_s, (x2, y2))

    pygame.draw.line(screen, GRAY, CENTER, (x1, y1), 6)  # hour
    pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 4)  # minute
    pygame.draw.line(screen, RED, (x2, y2), (x3, y3), 2)  # second

    return t

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(get_background_color())

    draw_clock_face()
    t = draw_pendulum_chain()

    # Digital time
    time_text = time.strftime("%H:%M:%S", t)
    date_text = time.strftime("%A, %d %B %Y", t)
    time_surf = font_digital.render(time_text, True, BLACK)
    date_surf = font_date.render(date_text, True, BLACK)

    screen.blit(time_surf, (WIDTH // 2 - time_surf.get_width() // 2, HEIGHT - 100))
    screen.blit(date_surf, (WIDTH // 2 - date_surf.get_width() // 2, HEIGHT - 60))

    pygame.display.flip()
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
root.destroy()
