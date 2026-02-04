
import pandas as pd

pd.set_option("display.max_columns", None)
# This line tells Pandas to display all columns of a DataFrame without hiding any.

df = pd.read_csv("data/students.csv")
print(df)