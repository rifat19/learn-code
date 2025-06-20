import pygame
import random
import math

# Initialize
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle Mesh")
clock = pygame.time.Clock()

# Particle Settings
num_particles = 100
max_distance = 100
particles = []

for _ in range(num_particles):
    particles.append({
        'x': random.randint(0, width),
        'y': random.randint(0, height),
        'vx': random.uniform(-1, 1),
        'vy': random.uniform(-1, 1)
    })

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BG_COLOR = (0, 0, 0)

# Main Loop
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for p in particles:
        # Update positions
        p['x'] += p['vx']
        p['y'] += p['vy']

        # Bounce from edges
        if p['x'] <= 0 or p['x'] >= width:
            p['vx'] *= -1
        if p['y'] <= 0 or p['y'] >= height:
            p['vy'] *= -1

        # Draw particle
        pygame.draw.circle(screen, WHITE, (int(p['x']), int(p['y'])), 2)

    # Draw mesh lines
    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            dx = particles[i]['x'] - particles[j]['x']
            dy = particles[i]['y'] - particles[j]['y']
            dist = math.hypot(dx, dy)

            if dist < max_distance:
                alpha = 255 - int((dist / max_distance) * 255)
                color = (255, 255, 255, alpha)
                surface = pygame.Surface((width, height), pygame.SRCALPHA)
                pygame.draw.line(surface, color,
                                 (int(particles[i]['x']), int(particles[i]['y'])),
                                 (int(particles[j]['x']), int(particles[j]['y'])))
                screen.blit(surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
