from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")

resume = """
Built REST APIs using FastAPI and Python.
"""

jd = """
Looking for backend developer with API development experience.
"""

resume_embedding = model.encode(resume)
jd_embedding = model.encode(jd)

score = cos_sim(
    resume_embedding,
    jd_embedding
)

print(score)