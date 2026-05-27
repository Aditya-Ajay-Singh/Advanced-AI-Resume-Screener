
skills_database = [
    "python",
    "machine learning",
    "deep learning",
    "tensorflow",
    "sql",
    "aws",
    "docker",
    "kubernetes",
    "linux",
    "cybersecurity",
    "networking",
    "penetration testing",
    "siem",
    "html",
    "css",
    "javascript",
    "react",
    "mongodb",
    "node.js",
    "power bi",
    "excel",
    "pandas",
    "data analysis",
    "terraform"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))
