
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/data/sales_data.csv")

monthly_sales = df.groupby("month")["revenue"].sum()
product_sales = df.groupby("product")["revenue"].sum()

# fig is a big container and axes is array of subplot objects.
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# subplots() → Creates multiple plots

# 2, 2 → 2 rows and 2 columns
# igsize=(12, 8) → width=12 inches, height=8 inches
# fig → Entire canvas
# axes → Grid of plot areas

# 1)Line Chart - Monthly Revenue
axes[0,0].plot(monthly_sales.index, monthly_sales.values)
axes[0,0].set_title("Monthly Revenue Trend")
axes[0,0].set_xlabel("Month")
axes[0,0].set_ylabel("Revenue")

# 2) Bar Chart

axes[0, 1].bar(product_sales.index, product_sales.values)

# 3) Histogram
axes[1, 0].hist(df["revenue"], bins=5) 
# Split data into 5 ranges.eg 0-100 like this.

# 4) Pie Chart
axes[1, 1].pie(product_sales.values, labels=product_sales.index, autopct="%1.1f%%")

plt.tight_layout()
# make neat spacing and prevents overlapping text and titles.
plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/subplots_dashboard.png")

plt.show()