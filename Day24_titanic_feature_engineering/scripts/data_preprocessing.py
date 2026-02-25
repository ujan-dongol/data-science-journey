import pandas as pd
import numpy as np

# load data 
df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day24_titanic_feature_engineering/data/titanics.csv")

print("Original Dataset SHpe:", df.shape)

# checking miss value
print("\nMissing Values:")
print(df.isnull().sum())


# Fill Age with median
df["age"].fillna(df["age"].median(), inplace=True)

# Fill Embarked with mode
df["embarked"].fillna(df["embarked"].mode()[0], inplace=True)

# Drop deck column (too many missing values)
df.drop(columns=["deck"], inplace=True)

# ---- Feature Engineering ---- #

# Create Family Size feature
df["family_size"] = df["sibsp"] + df["parch"] + 1

# Convert sex to numeric
df["sex"] = df["sex"].map({"male": 0, "female": 1})

# One-hot encode Embarked
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)

print("\nProcessed Dataset Shape:", df.shape)
print("\nFirst 5 rows after preprocessing:")
print(df.head())

# Save processed file
df.to_csv("C:/Users/Asus/Desktop/datascience/Day24_titanic_feature_engineering/outputs/titanic_data_processed.csv", index=False)

print("\nPreprocessing completed successfully!")