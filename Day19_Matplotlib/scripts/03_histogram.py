import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/data/sales_data.csv")

plt.figure()

plt.hist(df["revenue"], bins=5)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")

plt.savefig("C:/Users/Asus/Desktop/datascience/Day19_Matplotlib/outputs/histogram.png")

plt.show()
