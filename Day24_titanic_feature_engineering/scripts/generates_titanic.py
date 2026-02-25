import seaborn as sns
import pandas as pd 


df = sns.load_dataset("titanic")

df.to_csv("C:/Users/Asus/Desktop/datascience/Day24_titanic_feature_engineering/data/titanics.csv", index=False)

print("Titanic dataset saved successfully as titanic.csv")