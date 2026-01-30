
numbers = [10, 20, 30, "abc"]

for x in numbers:
    try:
        print(int(x))
    except ValueError:
        print("Invalid number:", x)