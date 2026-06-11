from resume_utils import *
from jd_utils import *

with open("skills.txt", "r") as file:
    skills = file.read().splitlines()

resume_file = input("Enter Resume PDF Name: ")

resume = extract_resume_text(resume_file)

found_skills = find_skills(resume, skills)

score = calculate_score(found_skills, resume)
#score = (len(found_skills) / len(skills)) * 100

print("Resume Score:", round(score, 2))    #Round the number to 2 digits after the decimal point.


print("\nSkills Found:")
for skill in found_skills:
    print("-", skill)


missing_skills = get_missing_skills(found_skills, skills)
#missing_skills = [skill for skill in skills if skill not in found_skills]

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)
 

print("\nSuggestions:")
suggestions = get_suggestions(resume)    

if suggestions:
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Resume looks good!") 

    
if score >= 80:
    print("\nExcellent Resume")
elif score >= 50:
    print("\nGood Resume")
else:
    print("\nNeeds Improvement")

jd_file = input("\nEnter Job Description File Name: ")

with open(jd_file, "r") as file:
    jd = file.read().lower()
    
print("\nJD Content:")
print(jd)    
    
match_score, matched_skills, missing_jd_skills, jd_skills = analyze_job_description(jd,skills,found_skills)

print("JD Skills:")
print(jd_skills)


print("\nMatch Score with Job Description:", round(match_score, 2), "%")
        
print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)
        
print("\nSkills in Job Description but Missing in Resume:")
for skill in missing_jd_skills:
    print("-", skill)
        
        