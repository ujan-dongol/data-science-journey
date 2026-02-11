
import numpy as np

salaries = np.array([30000, 45000, 60000, 80000])

# Vectorized increment
updated_salaries = salaries + 500

# Vectorized tax deduction (10%)
tax = salaries * 0.10
net_salary = salaries - tax


print("Original:", salaries)
print("Updated:", updated_salaries)
print("Net Salary:", net_salary)