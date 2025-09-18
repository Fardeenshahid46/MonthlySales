import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Sales Trend Dashboard", layout="centered")

st.title("📈 Company Sales Trend Over the Month")
st.write("Upload a CSV file with `Month` and `Sales` columns to view the trend.")

# ---- File Upload ----
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Read the uploaded CSV
    df = pd.read_csv(uploaded_file)

    # Optional: Preview data
    st.subheader("📋 Data Preview")
    st.dataframe(df)

    # ---- Plot the line chart ----
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df["Month"], df["Sales"], marker='o', linestyle='-', linewidth=2)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")
    ax.set_title("Company Sales Trend Over the Year")
    ax.grid(True)

    st.pyplot(fig)   # Display Matplotlib figure inside Streamlit

    # ---- Extra: Show basic stats ----
    st.subheader("📊 Sales Statistics")
    st.write("**Total Sales:**", df["Sales"].sum())
    st.write("**Average Monthly Sales:**", round(df["Sales"].mean(), 2))
else:
    st.info("Please upload a CSV file to see the chart.")
