
def students_result(name, marks):
    total = sum(marks)
    average = total / len(marks)
    
    return{
        "name": name,
        "marks": marks,
        "total": total,
        "average": average
    }
    
marks = [78, 85, 90]

result = students_result("Ujan Singh Dngl", marks)

for key,value in result.items():
    print(key, ":", value)    