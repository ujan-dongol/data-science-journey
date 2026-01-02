name = input("Enter Your Name : ")

Science = float(input("Enter Your Marks at Science : "))
Math = float(input("Enter Your Marks at Math : "))
English = float(input("Enter Your Marks at English : "))

total = Science + Math + English
percentage = total / 3

if percentage >= 40 :
    print("You have pass the exam .")
    
else:
    print("You have been fail this time .")


