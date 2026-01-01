name = input("Enter Your Name : ")

Science = int(input("Enter Your Marks for Science : "))
English = int(input("Enter Your Marks For English : "))
Math = int(input("Enter Your Marks For Math : "))

total_marks = Science + English + Math
percentage = total_marks / 3
gpa = (percentage / 100 ) * 4


print("\n----------Result will be ready soon--------------")
print(f"Student Name : {name}")
print(f"Total Marks You have got     : {total_marks}")
print(f"Percentage You have Secured  : {percentage :.2f}")
print(f"Congratulation! You have been secured {gpa :.2f}.")