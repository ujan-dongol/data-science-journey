

def grade (percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B+"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C+"
    elif percent >= 40:
        return "C"
    elif percent >= 30:
        return "D"
    else:
        return "Sorry You Have been fail this this better luck next time."
    
    
def result(percent):
    if percent >= 40:
        return "Congratulation ! You Have Passed Your Exam."
        
    else:
        return "So Sorry you have been not been passed Your Exam ."
        
        
percent = 45
print("Grade :", grade(percent))
print("Result:", result(percent))
