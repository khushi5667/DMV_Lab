import matplotlib.pyplot as plt
import numpy as np

# Taking input from user
start = float(input("Enter starting value: "))
end = float(input("Enter ending value: "))
points = int(input("Enter number of points: "))

# Generate values dynamically
x = np.linspace(start, end, points)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

# Plot Sine Wave
ax1.plot(x, y1)
ax1.set_title("Sine Wave")

# Plot Cosine Wave
ax2.plot(x, y2)
ax2.set_title("Cosine Wave")

plt.show()
