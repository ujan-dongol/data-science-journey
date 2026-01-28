
file = open("marks.txt", "r")
marks = file.readline()
file.close()

numbers = []


with open("marks.txt", "r") as file:
    for marks in file:
        marks = marks.strip()
        if marks != "":
            numbers.append(int(marks))

print(numbers)