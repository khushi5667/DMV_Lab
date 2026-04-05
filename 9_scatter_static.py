import matplotlib.pyplot as plt

# Predefined data
x_values = [1, 2, 3, 4, 5]
y_values = [5, 3, 7, 2, 6]

plt.scatter(x_values, y_values, color='red')
plt.title("Static Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
