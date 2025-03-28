import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("cleaned_production_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Streamlit Title
st.title("📊 Chemical Manufacturing Dashboard")

# Sidebar Filters
st.sidebar.header("Filter Data")
selected_date = st.sidebar.date_input("Select Date Range", [df["Date"].min(), df["Date"].max()])
df_filtered = df[(df["Date"] >= pd.to_datetime(selected_date[0])) & (df["Date"] <= pd.to_datetime(selected_date[1]))]

# Production Units Chart
st.subheader("📌 Production Units Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=df_filtered["Date"], y=df_filtered["Production_Units"], marker="o", ax=ax)
plt.xlabel("Date")
plt.ylabel("Production Units")
st.pyplot(fig)

# Sales Units Chart
st.subheader("📌 Sales Units Trend")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=df_filtered["Date"], y=df_filtered["Sales_Units"], marker="o", ax=ax, color="green")
plt.xlabel("Date")
plt.ylabel("Sales Units")
st.pyplot(fig)

# Defect Rate Scatter Plot
st.subheader("📌 Defect Rate vs Production Units")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=df_filtered["Production_Units"], y=df_filtered["Defect_Rate(%)"], color="red", ax=ax)
plt.xlabel("Production Units")
plt.ylabel("Defect Rate (%)")
st.pyplot(fig)

# Machine Downtime Bar Chart
st.subheader("📌 Machine Downtime Per Day")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=df_filtered["Date"].dt.strftime("%Y-%m-%d"), y=df_filtered["Machine_Downtime(Hours)"], color="purple", ax=ax)
plt.xticks(rotation=90)
plt.xlabel("Date")
plt.ylabel("Machine Downtime (Hours)")
st.pyplot(fig)

# Summary Statistics
st.subheader("📌 Summary Statistics")
st.write(df_filtered.describe())

