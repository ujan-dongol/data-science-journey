
# # 1) Loop with Dictionary


# dic ={
#     "Math" : 33,
#     "Science" : 45,
#     "English" : 67,
#     "Nepali" : 78,
#     "Chemistry" : 90,
    
# }

# for subject, score in dic.items():
#     print(f"{subject} => {score}.")
    
# #Output
# # Math => 33.
# # Science => 45.
# # English => 67.
# # Nepali => 78.
# # Chemistry => 90.    
    
    
    
# person ={
#     "name" : "Ujan",
#     "Location" : "Teku",
#     "Age" : 21
# }    

# for k,v in person.items():
#     print(k, "=" ,v)        
# # Output 
# # name = Ujan
# # Location = Teku
# # Age = 21


# Filtering Data

numbers = [3, 5, 6, 77, 83]

for num in numbers:
    if num > 100:
        print(f"Number :{num}.")
        
print("Numbers greater than 10")        