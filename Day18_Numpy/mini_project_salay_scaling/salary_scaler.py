import numpy as np

# Monthly salaries
monthly_salary = np.array([30000, 45000, 60000, 80000])

# Annual bonus percentage
bonus_rate = 0.20

# Broadcasting bonus calculation
annual_bonus = monthly_salary * bonus_rate

final_salary = monthly_salary + annual_bonus

print("Monthly Salary:", monthly_salary)
print("Annual Bonus:", annual_bonus)
print("Final Salary:", final_salary)
