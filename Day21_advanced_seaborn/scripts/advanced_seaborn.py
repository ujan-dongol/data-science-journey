import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/data/sales_data.csv")

sns.set_theme(style="whitegrid", context="notebook")

# FaceGrid Example

g = sns.FacetGrid(df , col="Region", height=4, aspect=1)
g.map_dataframe(sns.scatterplot, x ="Sales", y="Profit")
plt.title("Sales Vs Profit by Region ", y = 1.05)
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/facegrid.png")
plt.show()

sns.relplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    col="Region",
    kind ="scatter",
    height=4,
    aspect=1
)
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/relplot.png")
plt.show()

sns.catplot(
      data=df,
    y="Sales",
    x="Region",
    hue="Category",
    col="Region",
    kind ="bar",
    height=5,
    aspect=1.2
)
plt.title("Average Sales by Region and Category")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/catplot.png")
plt.show()

sns.displot(
    data=df,
    x="Sales",
    col="Region",
    kde=True,
    height=4,
    aspect=1
)
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/displot.png")
plt.show()

g = sns.PairGrid(df[["Sales", "Profit", "Quantity"]])
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
plt.savefig("C:/Users/Asus/Desktop/datascience/Day21_advanced_seaborn/outputs/pairgrid.png")
plt.show()