
def analyze_marks(filename):
    file = open(filename, "r")
    data = file.readlines()
    file.close()
    
    marks =[]
    
    
    for value in data:
        marks.append(int(value.strip()))
    
    
    result = {
        "Total": sum(marks),
        "Average": sum(marks) / len(marks), 
        "Highest": max(marks),
        "Lowest": min(marks)
     }    
    return result   



analysis = analyze_marks("data_of_miniproject.txt")

for key, value in analysis.items():
    print(key, ":", value)