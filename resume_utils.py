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


def get_suggestions(resume):

    suggestions = []

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
         
    return suggestions


def calculate_ats_score(resume, found_skills):

    ats_score = 0

    ats_score += min(len(found_skills) * 5, 50)

    if "projects" in resume:
        ats_score += 10

    if "education" in resume:
        ats_score += 10

    if "experience" in resume:
        ats_score += 10

    if "github" in resume:
        ats_score += 10

    if "linkedin" in resume:
        ats_score += 10

    if ats_score > 100:
        ats_score = 100

    return ats_score

def recommend_role(found_skills):

    roles = {
        "Frontend Developer": ["html", "css", "javascript"],
        "Backend Developer": ["python", "git", "api"],
        "Data Analyst": ["python", "sql"],
        "Machine Learning Engineer": ["python", "machine learning"]
    }

    best_role = "No Clear Recommendation"
    highest_score = 0

    role_scores = {}

    for role, role_skills in roles.items():

        matched = 0

        for skill in role_skills:
            if skill in found_skills:
                matched += 1

        percentage = (matched / len(role_skills)) * 100

        role_scores[role] = round(percentage, 2)

        if percentage > highest_score:
            highest_score = percentage
            best_role = role

    return best_role, role_scores