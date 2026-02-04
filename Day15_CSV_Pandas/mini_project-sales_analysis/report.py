
import pandas as pd

df = pd.read_csv("sales_report.csv")

total_revenue = df["revenue"].sum()

best_product = df.groupby("product")["revenue"].sum().idxmax()

daily_sales = df.groupby("date")["revenue"].sum()

print("Total Revenue:", total_revenue)
print("Best Selling Product:", best_product)
print("\nDaily Sales:")
print(daily_sales)