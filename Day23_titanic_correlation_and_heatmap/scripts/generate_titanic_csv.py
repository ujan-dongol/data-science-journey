import seaborn as sns
import pandas as pd 


df = sns.load_dataset("titanic")

df.to_csv("C:/Users/Asus/Desktop/datascience/Day23_titanic_correlation_and_heatmap/data/titanic.csv", index=False)

print("Titanic dataset saved successfully as titanic.csv")