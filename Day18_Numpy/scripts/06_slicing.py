
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[1:4])
# Start : index 1
# End : index 4 (NOT included)
print(arr[:3])  
# From start Till index 2 

print(arr[3:])
# From index 3 Till end

print(arr[::2])
# Skip every 2nd element
