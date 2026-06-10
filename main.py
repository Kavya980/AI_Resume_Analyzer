from PyPDF2 import PdfReader

def extract_resume_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text.lower()


def find_skills(resume, skills):

    found_skills = []

    for skill in skills:
        if skill in resume:
            found_skills.append(skill)

    return found_skills


def get_missing_skills(found_skills, skills):
    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    return missing_skills

def calculate_score(found_skills, resume):

    score = len(found_skills) * 5

    if "projects" in resume:
        score += 20

    if "github" in resume:
        score += 10

    if "linkedin" in resume:
        score += 10

    if "education" in resume:
        score += 5

    if "experience" in resume:
        score += 5

    if score > 100:
        score = 100

    return score

def get_suggestions(resume):

    suggestions = []

    print("\nSuggestions:")
    if "projects" not in resume:
        suggestions.append("Add Projects Section")

    if "github" not in resume:
        suggestions.append("Add GitHub Profile")

    if "linkedin" not in resume:
        suggestions.append("Add LinkedIn Profile")

    if "education" not in resume:
        suggestions.append("Add Education Section")

    if "experience" not in resume:
        suggestions.append("Add Experience Section")
        
    if suggestions:
      for suggestion in suggestions:
       print("-", suggestion)

    else:
      print("Resume looks good!")  
    return suggestions





with open("skills.txt", "r") as file:
    skills = file.read().splitlines()


resume_file = input("Enter Resume PDF Name: ")

resume = extract_resume_text(resume_file)

found_skills = find_skills(resume, skills)


    
score = calculate_score(found_skills, resume)
#score = (len(found_skills) / len(skills)) * 100

if score > 100:
    score = 100
print("Resume Score:", round(score, 2))    #Round the number to 2 digits after the decimal point.

print("\nSkills Found:")
for skill in found_skills:
    print("-", skill)





missing_skills = get_missing_skills(found_skills, skills)
#missing_skills = [skill for skill in skills if skill not in found_skills]

print("\nMissing Skills:")
for skill in missing_skills:
    print("-", skill)
    
    
 
    
suggestions = get_suggestions(resume)    
    
    
    
if score >= 80:
    print("Excellent Resume")
elif score >= 50:
    print("Good Resume")
else:
    print("Needs Improvement")

jd_file = input("Enter Job Description File Name: ")

with open(jd_file, "r") as file:
    jd = file.read().lower()
    
print("\nJD Content:")
print(jd)    
    
jd_skills = []

for skill in skills:
    if skill in jd:
        jd_skills.append(skill)   #found skills in the job description and added to jd_skills list

print("JD Skills:")
print(jd_skills)

        
matched_skills = []

for skill in found_skills:
    if skill in jd_skills:    
        matched_skills.append(skill)     #matched skills between resume and job description
       

if len(jd_skills) > 0:
    match_score = (len(matched_skills) / len(jd_skills))*100
else:
    match_score = 0
print("\nMatch Score with Job Description:", round(match_score, 2), "%")
        
print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)
    
    
missing_jd_skills = []

for skill in jd_skills:
    if skill not in found_skills:
        missing_jd_skills.append(skill)
        
print("\nSkills in Job Description but Missing in Resume:")
for skill in missing_jd_skills:
    print("-", skill)
        




       

      
        
        
        
        
        
        
        