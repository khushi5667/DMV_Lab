import matplotlib.pyplot as plt 
n= int(input("Enter number of subjects: "))

subjects = []
marks = []

for i in range(n):
    sub = input(f"Enter subjects {i+1} name: ")
    marks = int(input(f"Enter marks for {sub}: "))

    subjects.append(sub)
    marks.append(marks)

    plt.bar(subjects, marks)

    plt.title("Student marks")
    plt.xlabels("Subjects")
    plt.ylabels("marks")

    plt.show()
