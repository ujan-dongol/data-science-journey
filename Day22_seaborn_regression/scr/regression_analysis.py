
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/data/sales_data.csv")

# theme
sns.set_theme(style="whitegrid", context="notebook")

# 1. linear Regression
plt.figure(figsize=(8, 8))
sns.regplot(data=df, x="Sales", y="Profit")
# Shows relationship between Sales and Profit with a line.
plt.title("Linear Regression : Sales vs Profit")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/outputs/linear_regression.png")
plt.show()

# 2. Regression separated by Category
sns.lmplot(
    data = df,
    x="Sales",
    y="Profit",
    hue="Category",
    height=6,
    aspect=1.2
)
plt.title("Regression by Category")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/outputs/regression.png")
plt.show()

# 3. Polynomial Regression

sns.regplot(data=df, x="Sales",y="Profit", order=2)
# order=2 → polynomial degree (curve instead of straight line)
plt.title("Polynomial Regression (Order 2)")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/outputs/polynomial_regression.png")
plt.show()
# Small sales → small profit growth
# Large sales → much higher profit growth

# 4. Residual Plot
plt.figure(figsize=(8, 5))
sns.residplot(data=df, x="Sales", y="Profit")
plt.title("Residual Plot")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/outputs/residual.png")
plt.show()
# The Dotted Line (Important!)

# The horizontal line at 0 means:
# Perfect prediction (no error)
# Points Explanation
# Each dot = one data point error.