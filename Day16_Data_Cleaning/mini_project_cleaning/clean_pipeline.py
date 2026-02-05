import pandas as pd

def load_data():
    return pd.read_csv("../data/dirty_sales_data.csv")

def clean_products(df):
    df["product"] = df["product"].str.strip().str.lower()
    return df

def handle_missing(df):
    df["price"] = df["price"].fillna(df["price"].mean())
    df["date"] = df["date"].fillna("2025-01-01")
    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def add_revenue(df):
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)
    df["revenue"] = df["quantity"] * df["price"]
    return df

def main():
    df = load_data()
    df = clean_products(df)
    df = handle_missing(df)
    df = remove_duplicates(df)
    df = add_revenue(df)

    df.to_csv("cleaned_output.csv", index=False)
    print("Pipeline executed successfully!")
    print(df.tail())

if __name__ == "__main__":
    main()
