
import pandas as pd 

df =pd.read_csv("../data/dirty_sales_data.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

print("\nRaw Data Preview:")
print(df.tail())
