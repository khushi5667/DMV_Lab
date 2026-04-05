import matplotlib.pyplot as plt

# Take number of data values from user
n = int(input("Enter number of data values: "))

data = []

# Taking input values
for i in range(n):
    value = int(input("Enter value: "))
    data.append(value)

# Number of bins for histogram
bins = int(input("Enter number of bins: "))

# Plot histogram
plt.hist(data, bins=bins)

plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Dynamic Histogram")

plt.show()
