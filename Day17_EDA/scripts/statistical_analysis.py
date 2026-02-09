
import pandas as pd 

df = pd.read_csv(
    "C:/Users/Asus/Desktop/datascience/Day17_EDA/data/cleaned_sales_data.csv"
)

print("Summary Statistics:")
print(df.describe())

print("\nTotal Revenue:", df["revenue"].sum())

print("\nAverage Price:", df["price"].mean())