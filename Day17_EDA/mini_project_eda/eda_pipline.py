import pandas as pd 

df = pd.read_csv(
    "C:/Users/Asus/Desktop/datascience/Day17_EDA/data/cleaned_sales_data.csv"
)

report = []

report.append(f"Total Rows: {df.shape[0]}")
report.append(f"Total Columns: {df.shape[1]}")
report.append(f"Total Revenue: {df['revenue'].sum()}")
report.append(f"Average Price: {df['price'].mean()}")

with open("eda_report.txt", "w") as file:
    for line in report:
        file.write(line + "\n")
       
       
print("EDA REport Generated")
       
        
        