# AI Resume Analyzer

An AI-powered web application that analyzes resumes, calculates ATS scores, performs keyword and semantic matching against job descriptions, recommends suitable career roles, and identifies skill gaps to improve employability.

Built using Flask, NLP techniques, Sentence Transformers, and cosine similarity for semantic resume-job matching.

## Features

* Resume PDF Upload
* ATS Score Calculation
* Job Description Matching
* AI Semantic Match Score
* Career Role Recommendation
* Career Fit Analysis
* Skill Gap Analysis
* Resume Improvement Suggestions
* Modern Responsive UI

## Tech Stack

* Python
* Flask
* HTML
* CSS
* JavaScript
* PyPDF2
* Sentence Transformers
* Scikit-learn

## How It Works

1. Upload a resume PDF.
2. Upload a job description file.
3. The system extracts resume text.
4. Skills are identified from the resume.
5. ATS score is calculated.
6. Resume skills are matched against the job description.
7. AI semantic similarity is calculated between the resume and job description.
8. Suitable career roles are recommended.
9. Missing skills and improvement suggestions are displayed.

## Project Structure

AI_Resume_Analyzer/

├── app.py

├── resume_utils.py

├── jd_utils.py

├── skills.txt

├── templates/

│ └── index.html

├── static/

│ └── style.css

└── uploads/

## Future Improvements

* PDF Report Export
* Resume History Database
* User Authentication
* Online Deployment

## Live Demo

https://ai-resume-analyzer-3awf.onrender.com


## Author

Kavya
