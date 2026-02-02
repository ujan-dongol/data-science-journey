
import data_loader
import analysis
import report

marks = data_loader.load_marks("students.txt")


total = analysis.calculate(marks)
average = analysis.calculate_avg(marks)

report.print_report(marks, total, average)