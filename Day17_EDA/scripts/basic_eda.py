
import pandas as pd 

df = pd.read_csv(
    "C:/Users/Asus/Desktop/datascience/Day17_EDA/data/cleaned_sales_data.csv"
)

print("Shape of data :", df.shape)
print("\nColumn names:")
print(df.columns)

print("\nData types: ")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())