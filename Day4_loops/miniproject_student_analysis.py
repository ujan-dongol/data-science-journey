marks = [35, 78, 90, 42, 60, 25, 88]

total = 0
pass_count = 0
fail_count = 0

for mark in marks:
    total += mark
    if mark >= 40:
        pass_count += 1
    else:
        fail_count += 1

average = total / len(marks)

# len(marks) → total number of students

# Average formula → sum ÷ count

print("Total Students:", len(marks))
print("Passed:", pass_count)
print("Failed:", fail_count)
print("Average Marks:", average)
