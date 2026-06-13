import os
import time
from flask import Flask, render_template, request

from resume_utils import *
from jd_utils import *

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        resume_file = request.files["resume"]
        jd_file = request.files["jd"]

        print("Resume filename:", resume_file.filename)
        print("JD filename:", jd_file.filename)

        # safe filenames
        resume_filename = str(int(time.time())) + "_" + resume_file.filename
        jd_filename = str(int(time.time())) + "_" + jd_file.filename

        resume_path = os.path.join(UPLOAD_FOLDER, resume_filename)
        jd_path = os.path.join(UPLOAD_FOLDER, jd_filename)

        resume_file.save(resume_path)
        jd_file.save(jd_path)

        with open("skills.txt", "r") as file:
            skills = file.read().splitlines()

        resume = extract_resume_text(resume_path)

        found_skills = find_skills(resume, skills)

        recommended_role, role_scores = recommend_role(found_skills)

        sorted_role_scores = sorted(
            role_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        ats_score = calculate_ats_score(resume, found_skills)

        missing_skills = get_missing_skills(found_skills, skills)

        suggestions = get_suggestions(resume)

        with open(jd_path, "r") as file:
            jd = file.read().lower()

        match_score, matched_skills, missing_jd_skills, jd_skills = analyze_job_description(
            jd,
            skills,
            found_skills
        )

        skill_gap_feedback = get_skill_gap_feedback(missing_jd_skills)

        return render_template(
            "index.html",
            analysis_done=True,
            ats_score=ats_score,
            recommended_role=recommended_role,
            role_scores=role_scores,
            sorted_role_scores=sorted_role_scores,
            found_skills=found_skills,
            missing_skills=missing_skills,
            suggestions=suggestions,
            match_score=match_score,
            matched_skills=matched_skills,
            missing_jd_skills=missing_jd_skills,
            skill_gap_feedback=skill_gap_feedback
        )

    return render_template(
        "index.html",
        analysis_done=False,
        ats_score=None,
        match_score=None,
        recommended_role=None,
        role_scores={},
        sorted_role_scores=[],
        found_skills=[],
        missing_skills=[],
        suggestions=[],
        matched_skills=[],
        missing_jd_skills=[],
        skill_gap_feedback=None
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)