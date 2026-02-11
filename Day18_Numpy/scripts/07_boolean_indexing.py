
import numpy as np

salaries = np.array([30000, 45000, 60000, 80000, 25000])

highsalary = salaries[salaries> 50000]

print(f"Higheast salary :", highsalary)