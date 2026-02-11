import numpy as np

# Employee salaries
salaries = np.array([30000, 45000, 60000])

# Tax rate (scalar)
tax_rate = 0.10

# Broadcasting tax rate across salaries
tax = salaries * tax_rate

net_salary = salaries - tax

print("Salaries:", salaries)
print("Tax:", tax)
print("Net Salary:", net_salary)
