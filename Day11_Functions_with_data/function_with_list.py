
def calculator_average(marks):
    total = sum(marks)
    av = total / len(marks)
    return av

student_marks = [78, 85, 90, 66]


result = calculator_average(student_marks)

print("Average:", result)
