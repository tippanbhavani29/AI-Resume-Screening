from sklearn.feature_extraction.text import TfidfVectorizer


def generate_vectors(jd_text, resume_text):

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [jd_text, resume_text]
    )

    return vectors