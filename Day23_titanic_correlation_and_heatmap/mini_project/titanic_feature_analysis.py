import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/data/titanic.csv")

numeric_data= df.select_dtypes(include=["int64", "float64"])
corr = numeric_data.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="viridis")
plt.title("Mini Project : Titanic Feature Correlation")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/outputs/titanicfeature_correalation.png")
plt.show()

plt.figure(figsize=(6, 5))
sns.scatterplot(data= df , x="fare", y="survived")
plt.title("Survival Vs Fare")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/outputs/survial_vs_fare.png")
plt.show()


plt.figure(figsize=(6, 5))
sns.scatterplot(data=df, x="age", y="survived")
plt.title("Durvival vs Age")
plt.savefig("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/outputs/Durvival_vs_Age.png")
plt.show()
