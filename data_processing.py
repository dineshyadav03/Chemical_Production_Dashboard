import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("production_data.csv")

# Display first 5 rows
print("Initial Data Preview:")
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values per Column:")
print(missing_values)

# Fill missing numerical values with the column mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Basic calculations
mean_values = df.mean(numeric_only=True)
std_values = df.std(numeric_only=True)

# Print calculations
print("\nMean Values for Each Column:")
print(mean_values)

print("\nStandard Deviation for Each Column:")
print(std_values)

# Save the cleaned data for further use
df.to_csv("cleaned_production_data.csv", index=False)
print("\nData cleaned and saved successfully.")
