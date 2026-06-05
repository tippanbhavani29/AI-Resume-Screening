from ai.preprocess import preprocess_text

from parser.parser import extract_pdf_text
jd_text = """
Looking for a Data Scientist with Python,
SQL and Machine Learning skills.
"""
clean_resume_text = extract_pdf_text(
    r"c:\Users\Bhavani\Downloads\TIPPANWAR BHAVANI_Doc (1).pdf"
)
clean_jd_text=preprocess_text(jd_text)

from ai.embeddings import generate_vectors
from ai.similarity import calculate_similarity

vectors = generate_vectors(
    clean_jd_text,
    clean_resume_text
)

score = calculate_similarity(vectors)

print("Match Score:", round(score * 100, 2), "%")

from ai.skill_gap import find_skill_gaps

required_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "AWS",
    "Docker"
]

missing = find_skill_gaps(
    required_skills,
    clean_resume_text
)

print(
    "Missing Skills:",
    missing
)

result = {
    "match_score": round(score * 100, 2),
    "missing_skills": missing
}

print(result)