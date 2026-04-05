import matplotlib.pyplot as plt

# Number of values
n = int(input("Enter number of data points: "))

x = []
y = []

# Taking input
for i in range(n):
    x_val = int(input("Enter X value: "))
    y_val = int(input("Enter Y value: "))
    x.append(x_val)
    y.append(y_val)

# Plot
plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Dynamic Line Chart")
plt.show()
