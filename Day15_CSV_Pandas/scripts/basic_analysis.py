
import pandas as pd

df = pd.read_csv("data/students.csv")

print("Average Math :", df["math"].mean())

print('Highest Science :', df["science"].max())
print("Lowest Computer :", df["computer"].min())
