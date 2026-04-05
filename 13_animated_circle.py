import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')  # Keep circle round

# Create a circle
circle = Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

# Update function for animation
def update(frame):
    circle.center = (frame, 5)  # Move horizontally
    return circle,

# Create animation
ani = FuncAnimation(fig, update, frames=range(11), interval=200, blit=True)
plt.show()
