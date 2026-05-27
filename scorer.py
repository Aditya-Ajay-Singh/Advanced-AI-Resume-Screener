
def calculate_score(resume_skills, jd_skills):

    if len(jd_skills) == 0:
        return 0

    matched = 0

    for skill in jd_skills:

        if skill in resume_skills:
            matched += 1

    score = (matched / len(jd_skills)) * 100

    return round(score, 2)


def missing_skills(resume_skills, jd_skills):

    missing = []

    for skill in jd_skills:

        if skill not in resume_skills:
            missing.append(skill)

    return missing
