import matplotlib.pyplot as plt

x_values = []
y_values = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    x_values.append(x)
    y_values.append(y)

plt.scatter(x_values, y_values, color='blue')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
