
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/data/sales_data.csv")

monthly_sales = df.groupby("month")["revenue"].sum()
# groupby("month") → group rows by month
# ["revenue"] → select revenue column
# .sum() → total revenue per month
plt.figure()

plt.plot(monthly_sales.index, monthly_sales.values)


plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/line_plot.png")

plt.show()