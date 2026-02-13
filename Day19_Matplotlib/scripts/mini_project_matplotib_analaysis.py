import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/data/sales_data.csv")

monthly_sales = df.groupby("month")["revenue"].sum()
product_sales = df.groupby("product")["revenue"].sum()

# Line Plot
plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Revenue")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/dashboard_monthly.png")
plt.show()

# Bar Chart
plt.figure()
plt.bar(product_sales.index, product_sales.values)
plt.title("Product Performance")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/dashboard_products.png")
plt.show()
