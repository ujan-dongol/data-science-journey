
marks = [78, 85, 90, 66]
total =  0

for x in marks:
    total += x
# total = total + x
# total = 0
# total = 0 + 78  → 78
# total = 78 + 85 → 163
# total = 163 + 90 → 253
# total = 253 + 66 → 319

average = total / len(marks)
# total = 319
# len(marks) = 4

print("Average Marks:", average)


