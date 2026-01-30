
while True:
    try:
        age = int(input("Enter Your Age: "))
        break
    except ValueError:
        print("Invalid input. Try again.")       
print("Your age is : ", age)        