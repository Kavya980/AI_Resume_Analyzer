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
