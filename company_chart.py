import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("company_dataset.csv")

# Remove rows where employees OR name is empty
df = df.dropna(subset=["employees", "name"])

# Convert employee ranges to numbers
df["Employees_Numeric"] = df["employees"].replace({
    "1 Lakh+ Employees (India)": 100000,
    "50k-1 Lakh Employees (India)": 75000,
    "10k-50k Employees (India)": 30000,
    "1k-5k Employees (India)": 3000
})

# Take first 50 companies
df = df.head(50)

# Plot pie chart
plt.figure(figsize=(10,10))
plt.pie(df["Employees_Numeric"], labels=df["name"], autopct='%1.1f%%')

plt.title("Employees Distribution (Top 50 Companies)")
plt.show()





# FIXED column names here 👇
df = df.dropna(subset=["name", "ratings", "ctype", "review_count"])

# Convert ratings
df["ratings"] = pd.to_numeric(df["ratings"], errors="coerce")

# Clean review_count (remove text like "k Reviews")
df["review_count"] = df["review_count"].astype(str).str.extract('(\d+\.?\d*)')
df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce")

df = df.dropna(subset=["ratings", "review_count"])

# -----------------------------------
# Funnel Chart
# -----------------------------------
rating_counts = df["ratings"].value_counts().sort_values(ascending=False)

plt.figure()
plt.barh(rating_counts.index.astype(str), rating_counts.values)
plt.gca().invert_yaxis()
plt.title("Funnel Chart (Rating-wise)")
plt.show()

# -----------------------------------
# Bar Chart
# -----------------------------------
plt.figure()
rating_counts.sort_index().plot(kind="bar")
plt.title("Bar Chart (Rating-wise)")
plt.show()

# -----------------------------------
# Line Chart
# -----------------------------------
df["ctype_code"] = pd.factorize(df["ctype"])[0]

plt.figure()
plt.plot(df["name"].head(20), df["ctype_code"].head(20))
plt.xticks(rotation=90)
plt.title("Line Chart (Company vs CType)")
plt.show()

# -----------------------------------
# Histogram
# -----------------------------------
plt.figure()
plt.hist(df["review_count"], bins=10)
plt.title("Histogram (Review Count)")
plt.show()