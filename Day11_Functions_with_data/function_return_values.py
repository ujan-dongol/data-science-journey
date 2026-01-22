
def cal(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average
    
    
marks = [80, 90, 70]

total, avg = cal(marks)

print("Total : ", total)
print("Average:", avg)    