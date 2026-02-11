import numpy as np

prices = np.array([80000, 2500, 800, 80000, 2400])

total_sales = np.sum(prices)
average_price = np.mean(prices)

print("Total Sales:", total_sales)
print("Average Price:", average_price)
