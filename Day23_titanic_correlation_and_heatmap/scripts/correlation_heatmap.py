import pandas as pd 
import seaborn  as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/data/titanic.csv")
print("First 5 rows of dataset:")
print(df.head())

numeric_df = df.select_dtypes(include=["int64", "float64"])

print("\n Numeric Columns:")
print(numeric_df.columns)

# Compute correlation matrix
corr_matrix = numeric_df.corr()
print(corr_matrix)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Titanic Dataset Correlation Heatmap")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/outputs/heatmap.png")
plt.show()


# corr_matrix → data
# annot=True → show numbers
# cmap="coolwarm" → color scheme
# linewidths=0.5 → grid spacing
