import numpy as np
import pandas as pd

df = pd.read_csv( "C:/Users/Asus/Desktop/datascience/Day18_Numpy/mini_project_salary_analysis/salaries.csv"
)

salaries = np.array(df["salary"])

top_3_salaries = salaries[-3:]
average_salary = np.mean(salaries)
highest_salary = np.max(salaries)
low_income = salaries[salaries < 40000]
highest_income =salaries[salaries >= 60000]

print("Top 3 Salaries:", top_3_salaries)
print("Average Salary:", average_salary)
print("Highest Salary:", highest_salary)
print("Low Income Employees:", low_income)
print("High Income Employees:", highest_income)