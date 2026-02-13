import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/data/sales_data.csv")

product_sales = df.groupby("product")["revenue"].sum()

plt.figure()

plt.bar(product_sales.index, product_sales.values)

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/bar_chart.png")

plt.show()
