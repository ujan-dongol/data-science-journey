

numbers = [1, 2, 3, 4, 5]
squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)


# practice.py

# 1. Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# 2. Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# 4. Pass / Fail
marks = [45, 30, 78, 22, 90]

for mark in marks:
    if mark >= 40:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

