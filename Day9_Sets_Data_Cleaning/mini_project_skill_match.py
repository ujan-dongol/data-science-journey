

job_skills = {"Python", "SQL", "Statistics", "Machine learning"}
user_skills = set()

n = int(input("How many skills do you learned or have? "))

for x in range(n):
    skill = input(f"Enter skill {x+1}: ")
    user_skills.add(skill)


match_skills = job_skills & user_skills
missing_skills = job_skills - user_skills


print("\n--- Skill Match Report ---")
print("Your Skills:", user_skills)
print("Matched Skills:", match_skills)
print("Missing Skills:", missing_skills)

# Output if skill does not match with job_skills
# How many skills do you learned or have? 3
# Enter skill 1: Java
# Enter skill 2: php
# Enter skill 3: nod

# --- Skill Match Report ---
# Your Skills: {'Java', 'nod', 'php'}   
# Matched Skills: set()
# Missing Skills: {'Python', 'SQL', 'Statistics', 'Machine learning'}


# Output if match with job_skills set
# How many skills do you learned or have? 4
# Enter skill 1: Python 
# Enter skill 2: SQL
# Enter skill 3: Statistics
# Enter skill 4: Machine learning

# --- Skill Match Report ---
# Your Skills: {'SQL', 'Python ', 'Machine learning', 'Statistics'}
# Matched Skills: {'SQL', 'Machine learning', 'Statistics'}
# Missing Skills: {'Python'}