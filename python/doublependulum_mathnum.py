import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Bar lengths
L1 = 2.0
L2 = 1.0

# Angular speeds
omega1 = 1
omega2 = 6

# Create angle arrays
frames = 360
angles1 = np.radians(np.arange(0, frames * omega1, omega1))
angles2 = np.radians(np.arange(0, frames * omega2, omega2))

# Setup plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
line1, = ax.plot([], [], 'ro-', lw=4)
line2, = ax.plot([], [], 'bo-', lw=4)

# Update function
def update(i):
    x1 = L1 * np.cos(angles1[i])
    y1 = L1 * np.sin(angles1[i])
    x2 = x1 + L2 * np.cos(angles2[i])
    y2 = y1 + L2 * np.sin(angles2[i])
    line1.set_data([0, x1], [0, y1])
    line2.set_data([x1, x2], [y1, y2])
    return line1, line2

ani = animation.FuncAnimation(fig, update, frames=frames, interval=20, blit=True)
plt.title("Linked Rotating Bars (Double Rotation)")
plt.show()
