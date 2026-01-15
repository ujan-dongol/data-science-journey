
student = {}

student["NAME"] = input("Enter name : ")
student["math"] = int(input("Math marks : "))
student["science"] = int(input("Science marks: "))
student["computer"] = int(input("Computer marks: "))

total = student["math"] + student["science"] + student["computer"]
average = total / 3

print("\n--- Result ---")
for key, value in student.items():
    print(key, ":", value)

print("Total:", total)
print("Average:", average)
                      