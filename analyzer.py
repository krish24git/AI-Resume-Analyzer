import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_resume(resume_text, jd_text):
    resume_doc = nlp(resume_text.lower())
    jd_doc = nlp(jd_text.lower())

    resume_tokens = {token.text for token in resume_doc if token.is_alpha}
    jd_tokens = {token.text for token in jd_doc if token.is_alpha}

    match = resume_tokens.intersection(jd_tokens)
    score = (len(match) / len(jd_tokens)) * 100 if jd_tokens else 0

    return round(score, 2), match
