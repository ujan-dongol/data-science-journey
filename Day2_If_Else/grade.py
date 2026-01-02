name = input("Enter Your Name : ")
course = input("Enter Your Course or Sem : ")
student_id = input("Enter Your Student id : ")

machine_learning= int(input("Write Your marks obtained at Machine Learning : "))
networking = int(input("Write Your marks obtained at Networking : "))
cloud = int(input("Write Your marks obtained at CloudComputing : "))
computer_research = int(input("Write Your marks obtaint at Computer Research : "))

total = machine_learning + networking + cloud + computer_research
percent = total / 4

if percent >= 90:
    grade = "A+"
elif percent >= 80:
    grade = "A"
elif percent >= 70:
    grade = "B+"
elif percent >= 60:
    grade = "B"
elif percent >= 50:
    grade = "C"
elif percent >= 40:
    grade = "D"
else:
    grade ="F"  
    
if percent >=40:
    result = "Pass"
else:
    result = "Fail" 
    
    
       
print("\n----------Student Result------------")
print(f"NAME          :  {name}") 
print(f"Course/Sem    :  {course}") 
print(f"Student ID    :  {student_id}")
print(f"Total Marks   :  {total}")  
print(f"Percentage    :  {percent:.2f}%")
print(f"Result        :  {result}") 
print(f"The Grade {name} got {grade}.") 


              
