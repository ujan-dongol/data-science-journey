import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Correlation matrix
corr = df.corr(numeric_only=True)

# Heatmap
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

# Pairplot
sns.pairplot(df, hue="sex")

plt.show()
