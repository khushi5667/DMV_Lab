import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("clv_data.csv")

print("Dataset Loaded Successfully!\n")

# Select numerical columns
data = df[['age', 'income', 'days_on_platform', 'purchases']]

# Create boxplot
plt.boxplot(data.values, labels=data.columns)

# Labels and title
plt.xlabel("Dataset Features")
plt.ylabel("Values")
plt.title("Box Plot for CLV Dataset")

# Show plot
plt.show()
