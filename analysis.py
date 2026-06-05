import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nTotal Profit:")
print(df["Profit"].sum())

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("plots/sales_by_category.png")

# Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()

print("\nProfit by Category:")
print(category_profit)

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("plots/profit_by_category.png")

print("\nGraphs saved successfully!")
# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("plots/sales_by_region.png")
# Top 10 Products by Sales
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Products by Sales:")
print(top_products)

plt.figure(figsize=(14,8))
top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.savefig("plots/top10_products_sales.png", bbox_inches="tight")
# Monthly Sales Trend

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("plots/monthly_sales_trend.png")
# Discount vs Profit

plt.figure(figsize=(8,5))

plt.scatter(df["Discount"], df["Profit"])

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.savefig("plots/discount_vs_profit.png")

print("\nDiscount vs Profit graph saved.")