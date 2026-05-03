import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
data_file = Path(__file__).resolve().parent / "data" / "Superstore.csv"
df = pd.read_csv(data_file, encoding="cp1252")

# ---------------------------
# DATA CLEANING
# ---------------------------

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ---------------------------
# ANALYSIS
# ---------------------------

# Total sales & profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

# Top 5 products
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Sales by region
sales_by_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Monthly sales trend
monthly_sales = (
    df.set_index("Order Date")
    .resample("ME")["Sales"]
    .sum()
)

# Loss-making products
loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(5)
)

monthly_sales.plot(title="Monthly Sales Trend")
plt.show()

# ---------------------------
# OUTPUT
# ---------------------------

print("=== SALES SUMMARY ===")
print(f"Total Sales: {total_sales}")
print(f"Total Profit: {total_profit}")

print("\n=== TOP PRODUCTS ===")
print(top_products)

print("\n=== SALES BY REGION ===")
print(sales_by_region)

print("\n=== MONTHLY SALES TREND ===")
print(monthly_sales.head())

print("\n=== LOSS-MAKING PRODUCTS ===")
print(loss_products)
