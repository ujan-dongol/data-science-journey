
try:
    file = open("marks.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("marks.txt file not found")
    
finally:
    print("File operation completed.")        
    
    
# Line 2
# file = open("marks.txt", "r")


# 👉 Python tries to:

# Open a file named marks.txt

# In read mode ("r")

# In the current folder (Day13_Error_Handling)

#  But in your case:

# marks.txt does not exist

# So Python raises this error internally:

# FileNotFoundError

# 🔹 What happens when the error occurs?

# 🚨 Important rule:

# When an error happens inside try, Python stops executing the rest of the try block.

# So this line is SKIPPED:

# print(file.read())

# 🔹 Line 4
# except FileNotFoundError:


# 👉 Python checks:

# “Is there an except that matches this error?”

# YES — FileNotFoundError matches exactly.

# So Python enters this block.

# 🔹 Line 5
# print("marks.txt file not found")
# marks.txt filr not found

# 🔹 Line 6
# finally: VERY IMPORTANT CONCEPT
# finally ALWAYS runs
# Whether there is an error or not    