
marks =[]

for i in range(5):
    try:
        mark = int(input(f"Enter mark {i+1} : "))
        marks.append(mark) 
    except ValueError:
        print("Invalid input, mark skipped.")
        
if marks:
    total = sum(marks)
    avg = total / len(marks)    
    
    
    print("\n ----Result----")
    print("Marks: ", marks)
    print("Average:", avg)

else:
    print("No valid marks entered")
        
            