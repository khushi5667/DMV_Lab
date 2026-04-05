import matplotlib.pyplot as plt

data = [10, 12, 15, 20, 22, 25, 25, 30, 32, 35, 40]

plt.hist(data, bins=5)
plt.xlabel("Data values")
plt.ylabel("Frequency")
plt.title("Simple Histogram")
plt.show()
