import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/data/sales_data.csv")

monthly_sales = df.groupby("month")["revenue"].sum()

plt.figure(figsize=(8,5))

plt.plot(monthly_sales.index, monthly_sales.values, marker="o", linestyle="--")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.grid(True)

plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/customized_plot.png")

plt.show()
