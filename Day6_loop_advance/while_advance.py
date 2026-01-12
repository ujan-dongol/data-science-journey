

password = ""

while password != "ujandatascience" :
    password = input("Enter password : ")
    
print("Access Granterd.")

# Output
# Enter password : ujan
# Enter password : ujandatascience
# Access Granterd.


choice = ""

while choice != "3":
    print("\n1. Say Hello")
    print("2. Show Numbers")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello, Ujan")
    elif choice == "2":
        for i in range(1, 6):
            print(i)
    elif choice == "3":
        print("Exiting program...")
    else:
        print("Invalid choice ")
