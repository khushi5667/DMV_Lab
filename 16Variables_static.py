import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

plt.plot(x,y, marker='o')

plt.xlabel("X values (independent variables)")
plt.ylabel("Y values (dependent variables)")

plt.title("X-Y Axis Data Plot")

plt.grid(True)
plt.show()
