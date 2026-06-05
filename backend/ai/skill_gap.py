def find_missing_keywords(
    jd_keywords,
    resume_text
):

    resume_text = resume_text.lower()

    missing = []

    for keyword in jd_keywords:

        if keyword.lower() not in resume_text:

            missing.append(keyword)

    return missing