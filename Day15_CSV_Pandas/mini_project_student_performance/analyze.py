import pandas as pd

df = pd.read_csv("../data/students.csv")

df["average"] = df[["math", "science", "computer"]].mean(axis=1)

top_student = df.loc[df["average"].idxmax()]

print("Top Student:")
print(top_student)
