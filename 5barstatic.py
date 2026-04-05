import matplotlib.pyplot as plt

subjects = ['math', 'science', 'english', 'computer', 'history']
marks = [80, 75, 90, 85, 70]

plt.bar(subjects, marks)
plt.title("Students marks")
plt.xlabel("subjects")
plt.ylabel("marks")

plt.show()
