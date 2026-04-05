import matplotlib.pyplot as plt

labels = []
values = []

n = int(input("Enter number of categories: "))

for i in range(n):
    label = input("Enter label: ")
    value = int(input("Enter value: "))
    
    labels.append(label)
    values.append(value)

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
