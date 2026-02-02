
import math_utils
import stats_utils

marks = [78, 85, 90]

print("Addition:", math_utils.add(5, 3))
print("Subtraction:", math_utils.sub(10, 5))

average = stats_utils.calculate_average(marks)
highest = stats_utils.find_max(marks)

print("Average Marks :", average)
print('Hightest Marks :', highest)