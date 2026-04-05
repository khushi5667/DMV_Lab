import matplotlib.pyplot as plt

x = []
y = []

n = int(input("Enter number of points: "))

for i in range(n):
    xv = int(input("Enter X value: "))
    yv = int(input("Enter Y value: "))
    x.append(xv)
    y.append(yv)

plt.plot(x, y, marker='o')

plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")
plt.title("X-Y Axis Data Plot")

plt.grid(False)
plt.show()
