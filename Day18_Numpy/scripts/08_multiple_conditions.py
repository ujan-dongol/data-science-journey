
import numpy as np

salaries = np.array([30000, 45000, 60000, 80000, 25000])

mid_salary = salaries[(salaries > 30000) & (salaries< 70000)]

print(mid_salary)