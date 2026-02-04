
import pandas as pd

df = pd.read_csv("../data/sales.csv")

df["revenue"] = df["quantity"] * df["price"]

df.to_csv("sales_report.csv", index = False)

print("Sales analysis have been completed")


