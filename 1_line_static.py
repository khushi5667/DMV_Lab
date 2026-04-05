import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 25, 35]

# Draw line chart
plt.plot(x, y)

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Line Chart")

# Show chart
plt.show()
