import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/data/sales_data.csv")
sns.set_theme(style="whitegrid")

print("Basic Statistics:")
print(df.describe())

# Regression
sns.lmplot(
    data= df,
    x="Sales",
    y="Profit",
    hue="Category",
    col="Region",
    height=5,
    aspect=1
)
plt.suptitle("Sales vs Profit Analysis by Region and Catagory", y=1.02)
plt.savefig("C:/Users/Asus/Desktop/datascience/Day22_seaborn_regression/outputs/miniproject_regression.png")
plt.show()


# Output
# Basic Statistics:
#           Order_ID        Sales     Profit   Quantity
# count    25.000000    25.000000   25.00000  25.000000
# mean   1013.000000   934.400000  171.52000   3.760000
# std       7.359801   400.458903  115.07176   1.392839
# min    1001.000000   400.000000   50.00000   2.000000
# 25%    1007.000000   620.000000   80.00000   3.000000
# 50%    1013.000000   850.000000  130.00000   4.000000
# 75%    1019.000000  1250.000000  250.00000   5.000000
# max    1025.000000  1700.000000  420.00000   7.000000