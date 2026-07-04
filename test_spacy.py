import spacy

nlp = spacy.load("en_core_web_sm")

text = """
I know Python, SQL, FastAPI and Machine Learning.
"""

doc = nlp(text)

for token in doc:
    print(token.text)
    