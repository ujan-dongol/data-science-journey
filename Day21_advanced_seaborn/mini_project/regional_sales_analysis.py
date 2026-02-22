
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/data/sales_data.csv")

sns.set_theme(style="darkgrid", context="talk")

# 1. Total Profit by Region
plt.figure()
sns.barplot(data=df, x="Region", y="Profit", estimator=sum)
plt.title("Total Profit by Region")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/totalprofitbyregion.png")
plt.show()

# 2. Sales Distribution by Category
sns.boxplot(data=df, x="Category", y="Sales")
plt.title("Sales Distribution by Category")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/Sales Distribution by Category.png")
plt.show()

# 3. Faceted Scatter Plot
sns.relplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    col="Region",
    kind="scatter"
)
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/facetedscatter.png")
plt.show()