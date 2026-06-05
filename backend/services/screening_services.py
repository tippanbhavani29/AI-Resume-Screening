from backend.ai.preprocess import preprocess_text
from backend.ai.embeddings import generate_vectors
from backend.ai.similarity import calculate_similarity
from backend.ai.key_extractor import extract_keywords
from backend.ai.skill_extractor import extract_skills


def process_resume(
    jd_text,
    resume_text
):

    clean_resume = preprocess_text(
        resume_text
    )

    clean_jd = preprocess_text(
        jd_text
    )

    vectors = generate_vectors(
        clean_jd,
        clean_resume
    )

    score = calculate_similarity(
        vectors
    )

    jd_keywords = extract_keywords(
        clean_jd
    )

    jd_skills = extract_skills(
        clean_jd
    )

    resume_skills = extract_skills(
        clean_resume
    )

    matched_skills = list(
        set(jd_skills)
        .intersection(
            set(resume_skills)
        )
    )

    missing_skills = list(
        set(jd_skills)
        -
        set(resume_skills)
    )

    if len(jd_skills) > 0:

        skill_match_score = round(
            (
                len(matched_skills)
                /
                len(jd_skills)
            ) * 100,
            2
        )

    else:

        skill_match_score = 0

    if skill_match_score >= 80:

        recommendation = (
            "Highly Recommended"
        )

    elif skill_match_score >= 60:

        recommendation = (
            "Recommended"
        )

    else:

        recommendation = (
            "Needs Review"
        )

    return {

        "overall_match_score":
            round(
                score * 100,
                2
            ),

        "skill_match_score":
            skill_match_score,

        "recommendation":
            recommendation,

        "jd_skills":
            jd_skills,

        "resume_skills":
            resume_skills,

        "matched_skills":
            matched_skills,

        "missing_skills":
            missing_skills,

        "important_jd_keywords":
            jd_keywords
    }