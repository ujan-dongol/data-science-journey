marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("\n--- Result ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
