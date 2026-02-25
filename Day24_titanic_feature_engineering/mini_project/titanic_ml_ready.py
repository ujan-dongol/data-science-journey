import pandas as pd

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day24_titanic_feature_engineering/data/titanics.csv")

print("Final ML-Ready Dataset Info:")
print(df.info())

print("\nChecking for remaining missing values:")
print(df.isnull().sum())

df.to_csv("C:/Users/Asus/Desktop/datascience/Day24_titanic_feature_engineering/outputs/miniproject_titanic_ml_ready.csv", index=False)
print("\nDataset ready for ML training!")