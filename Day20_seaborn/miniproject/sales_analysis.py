import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Furniture", "Furniture"],
    "Sales": [500, 300, 700, 200, 400, 600],
    "Profit": [50, 30, 90, 20, 40, 80]
}

df = pd.DataFrame(data)

# Sales by category
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.show()

# Distribution of sales
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.show()

# Correlation heatmap
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Sales-Profit Correlation")
plt.show()
