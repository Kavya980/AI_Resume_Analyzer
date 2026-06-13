from flask import Flask, render_template, request   
#,app would have make an object of Flask class, render_template would allow us to render html files and request would allow us to handle form data

from resume_utils import *
from jd_utils import *

app = Flask(__name__)
#Create MY website and store it in variable app

@app.route("/", methods=["GET", "POST"])   
#@app.route("/") would allow us to define the route for our website, in this case it is the home page ("/"). methods=["GET", "POST"] allows us to handle both GET and POST requests for this route.

def home():
    if request.method == "POST":

      resume_file = request.files["resume"]
      jd_file = request.files["jd"]

      resume_path = "uploads/" + resume_file.filename
      jd_path = "uploads/" + jd_file.filename

      resume_file.save(resume_path)
      jd_file.save(jd_path)
     
      with open("skills.txt", "r") as file:
       skills = file.read().splitlines()
     
      resume = extract_resume_text(resume_path)

      found_skills = find_skills(resume, skills)
      
      recommended_role = recommend_role(found_skills)
      
      ats_score = calculate_ats_score(resume, found_skills)

      missing_skills = get_missing_skills(found_skills, skills)

      suggestions = get_suggestions(resume)
     
      print("Resume Saved:", resume_path)
      print("JD Saved:", jd_path)
      
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
      ats_score=ats_score,
      recommended_role=recommended_role,
      found_skills=found_skills,
      missing_skills=missing_skills,
      suggestions=suggestions,
      match_score=match_score,
      matched_skills=matched_skills,
      missing_jd_skills=missing_jd_skills,
      skill_gap_feedback=skill_gap_feedback,
      )
          
    return render_template("index.html")
#Open index.html and send it to browser

app.run(debug=True)