
import pandas as pd 

df = pd.read_csv("../data/students.csv")

df["average"] = df[["math", "science", "computer"]].mean(axis=1)

df.to_csv("final_report.csv", index=False)

print("Report generated: final_report.csv")

# Break it:
# Part	                    Meaning
# df.to_csv()	            save DataFrame
# "final_report.csv"	    output file
# index=False	            don’t save row numbers