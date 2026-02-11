import numpy as np

data = np.array([10, 20, 30, 40])

# Using loop
loop = []

for x in data:
    loop.append(x * 2)
    
#Using vectorization
vector_result = data * 2

print("Loop Result:", loop)
print("Vector Result:", vector_result)

# Output 
# Loop Result: [np.int64(20), np.int64(40), np.int64(60), np.int64(80)]
# Vector Result: [20 40 60 80]