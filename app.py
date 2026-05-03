from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Superstore Sales Dashboard", layout="wide")
st.title("Superstore Sales Dashboard")
st.caption("Data cleaning and sales analysis portfolio demo")


@st.cache_data
def load_data() -> pd.DataFrame:
    data_file = Path(__file__).resolve().parent / "data" / "Superstore.csv"
    df = pd.read_csv(data_file, encoding="cp1252")
    df = df.drop_duplicates().copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df = df.dropna(subset=["Order Date"])
    return df


df = load_data()

total_sales = float(df["Sales"].sum())
total_profit = float(df["Profit"].sum())

top_products = (
    df.groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(5)
)

sales_by_region = (
    df.groupby("Region", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

monthly_sales = (
    df.set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
    .rename("Sales")
    .to_frame()
)

loss_products = (
    df.groupby("Product Name", as_index=False)["Profit"]
    .sum()
    .query("Profit < 0")
    .sort_values("Profit", ascending=True)
    .head(5)
)

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")

left, right = st.columns(2)

with left:
    st.subheader("Top 5 Products by Sales")
    st.dataframe(top_products, use_container_width=True, hide_index=True)
    st.bar_chart(top_products.set_index("Product Name")["Sales"])

with right:
    st.subheader("Sales by Region")
    st.dataframe(sales_by_region, use_container_width=True, hide_index=True)
    st.bar_chart(sales_by_region.set_index("Region")["Sales"])

st.subheader("Monthly Sales Trend")
st.line_chart(monthly_sales)

st.subheader("Top 5 Loss-Making Products")
if loss_products.empty:
    st.success("No loss-making products found.")
else:
    st.dataframe(loss_products, use_container_width=True, hide_index=True)
