# Day 13: Error Handling in Python

## Overview
Day 13 focuses on **handling runtime errors safely** using Python’s
`try`, `except`, `else`, and `finally` blocks.

Error handling is essential in:
- Data Science (dirty or missing data)
- Backend systems (user input, files, APIs)
- Real-world applications (no crashes)

---

## Topics Covered

### 1. try / except Basics
- Prevent program crashes
- Handle unexpected user input
- Graceful failure handling

### 2. Handling Common Errors
- `ValueError` (invalid input / type conversion)
- `ZeroDivisionError`
- `FileNotFoundError`

### 3. finally Block
- Executes **always**
- Used for cleanup and status messages

### 4. Safe User Input
- Repeated input until valid data is entered
- Improves user experience

### 5. Data Cleaning with Error Handling
- Skip invalid data
- Prepare clean datasets
- Core data science concept

---

## Files Included

- `basic_try_except.py`  
  → Basic try/except usage

- `input_error.py`  
  → Handling invalid user input

- `file_error.py`  
  → Safe file handling with finally block

- `practice.py`  
  → Cleaning mixed/invalid data

- `mini_project_safe_marks.py`  
  → Real-world mini project with safe inputs

---

## Additional Practice Added

### Safe Input Loop
```python
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input. Try again.")
