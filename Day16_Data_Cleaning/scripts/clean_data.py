import pandas as pd

# Load dirty data
df = pd.read_csv("../data/dirty_sales_data.csv")

# Clean product names
df["product"] = df["product"].str.strip().str.lower()

# Fill missing price with average
df["price"] = df["price"].fillna(df["price"].mean())

# Fill missing date
df["date"] = df["date"].fillna("2025-01-01")

# Remove duplicates
df = df.drop_duplicates()

# Fix data types
df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(float)

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

print("Cleaned Data:")
print(df.tail())
