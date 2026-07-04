from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_match_score(resume_text, jd_text):

    resume_embedding = model.encode(resume_text)

    jd_embedding = model.encode(jd_text)

    score = cos_sim(
        resume_embedding,
        jd_embedding
    )

    return round(float(score[0][0]) * 100, 2)


def analyze_job_description(jd, skills, found_skills):

    jd_skills = []

    for skill in skills:
        if skill in jd:
            jd_skills.append(skill)

    matched_skills = []

    for skill in found_skills:
        if skill in jd_skills:
            matched_skills.append(skill)

    missing_jd_skills = []

    for skill in jd_skills:
        if skill not in found_skills:
            missing_jd_skills.append(skill)

    if len(jd_skills) > 0:
        match_score = (len(matched_skills) / len(jd_skills)) * 100
    else:
        match_score = 0

    return match_score, matched_skills, missing_jd_skills, jd_skills


def get_skill_gap_feedback(missing_jd_skills):

    if len(missing_jd_skills) == 0:
        return "Excellent! Your resume covers all required skills."

    feedback = (
        f"You are missing {len(missing_jd_skills)} required skill(s). "
        "Recommended learning order:"
    )

    return feedback