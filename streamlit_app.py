import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Retail & Macro Trend Dashboard", layout="wide")
st.title("📊 Retail & Macro Trend Dashboard")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/sample_retail.csv")
    except FileNotFoundError:
        st.error("Sample data not found. Please add a small CSV file in data/ folder.")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Total Sales Over Time")
    fig = px.line(df, x="date", y="sales", title="Total Sales Trend")
    st.plotly_chart(fig, use_container_width=True)
