import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="Chemical Production Dashboard", layout="wide")

# Sidebar with logo
st.sidebar.image("assets/logo.png", width=150)  # Ensure correct path

# Sidebar navigation
selected = option_menu(
    menu_title="Navigation",
    options=["Dashboard", "Production Trends", "Raw Materials", "Quality Control"],
    icons=["bar-chart", "line-chart", "boxes", "clipboard-check"],
    menu_icon="menu-app",
    default_index=0,
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_production_data.csv")  # Ensure correct path
    df["Date"] = pd.to_datetime(df["Date"]).dt.date  # Convert Timestamp to datetime.date
    return df

df = load_data()

# Main Dashboard Content
if selected == "Dashboard":
    st.title("Chemical Production Overview")

    # Date Filter
    min_date, max_date = st.slider(
        "Select Date Range:", 
        min_value=min(df["Date"]), 
        max_value=max(df["Date"]), 
        value=(min(df["Date"]), max(df["Date"]))
    )

    # Apply date filter
    filtered_df = df[(df["Date"] >= min_date) & (df["Date"] <= max_date)]

    # KPI Metricss
    total_production = filtered_df["Production_Units"].sum()
    avg_defect_rate = filtered_df["Defect_Rate(%)"].mean()

    col1, col2 = st.columns(2)
    col1.metric("Total Production (Units)", f"{total_production:,.0f}")
    col2.metric("Average Defect Rate (%)", f"{avg_defect_rate:.2f}")

    # Production Trends
    fig = px.line(
        filtered_df, x="Date", y="Production_Units",
        title="📈 Production Units Over Time",
        labels={"Production_Units": "Units"}
    )
    st.plotly_chart(fig, use_container_width=True)

# Additional Sections
elif selected == "Production Trends":
    st.title("📊 Production Trends Analysis")
    fig = px.bar(df, x="Date", y="Production_Units", title="📊 Daily Production")
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Raw Materials":
    st.title("📦 Raw Materials Usage")
    fig = px.pie(df, names="Sales_Units", values="Production_Units", title="⚖️ Sales vs Production")
    st.plotly_chart(fig, use_container_width=True)

elif selected == "Quality Control":
    st.title("🔬 Quality Control Insights")
    fig = px.scatter(df, x="Date", y="Defect_Rate(%)", title="📏 Defect Rate Over Time")
    st.plotly_chart(fig, use_container_width=True)
