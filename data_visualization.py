import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
df = pd.read_csv("cleaned_production_data.csv")

# Print column names to verify
print("Columns in DataFrame:", df.columns)

# Ensure column names match exactly
expected_columns = ["Date", "Production_Units", "Sales_Units", "Defect_Rate(%)", "Machine_Downtime(Hours)"]
df.columns = [col.strip() for col in df.columns]  # Remove any extra spaces

# Convert "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Plot Production Units Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Production_Units"], bins=20, kde=True, color="blue")
plt.xlabel("Production Units")
plt.ylabel("Frequency")
plt.title("Distribution of Production Units")
plt.show()

# Plot Sales Units Trend Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["Date"], y=df["Sales_Units"], marker="o", color="green")
plt.xlabel("Date")
plt.ylabel("Sales Units")
plt.title("Sales Units Over Time")
plt.xticks(rotation=45)
plt.show()

# Scatter plot of Defect Rate vs Production Units
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Production_Units"], y=df["Defect_Rate(%)"], color="red")
plt.xlabel("Production Units")
plt.ylabel("Defect Rate (%)")
plt.title("Defect Rate vs Production Units")
plt.show()

# Bar chart for Machine Downtime
plt.figure(figsize=(8, 5))
sns.barplot(x=df["Date"].dt.strftime("%Y-%m-%d"), y=df["Machine_Downtime(Hours)"], color="purple")
plt.xlabel("Date")
plt.ylabel("Machine Downtime (Hours)")
plt.title("Machine Downtime Per Day")
plt.xticks(rotation=90)
plt.show()
