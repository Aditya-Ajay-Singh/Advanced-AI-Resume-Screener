
import streamlit as st
import pandas as pd
from parser import extract_text
from skill_extractor import extract_skills
from scorer import calculate_score, missing_skills

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# Sidebar
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Resume Screening", "Available Jobs"]
)

# Job Database
jobs = {
    "AI/ML Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "SQL",
        "AWS",
        "Docker"
    ],
    "Cybersecurity Analyst": [
        "Linux",
        "Cybersecurity",
        "Python",
        "Networking",
        "SIEM",
        "Penetration Testing"
    ],
    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "MongoDB",
        "Node.js"
    ],
    "Data Analyst": [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Pandas",
        "Data Analysis"
    ],
    "Cloud Engineer": [
        "AWS",
        "Docker",
        "Kubernetes",
        "Linux",
        "Terraform",
        "Python"
    ]
}

if page == "Resume Screening":

    st.title("📄 AI Resume Screening System")
    st.markdown("### Smart ATS Resume Analyzer using NLP & Machine Learning")

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader(
            "Upload Resume (PDF)",
            type=["pdf"]
        )

    with col2:
        selected_job = st.selectbox(
            "Select Job Role",
            list(jobs.keys())
        )

    st.write("### Required Skills")
    st.info(", ".join(jobs[selected_job]))

    jd_text = " ".join(jobs[selected_job])

    if resume_file:

        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())

        resume_text = extract_text("temp_resume.pdf")

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        score = calculate_score(resume_skills, jd_skills)
        missing = missing_skills(resume_skills, jd_skills)

        st.divider()

        metric1, metric2 = st.columns(2)

        with metric1:
            st.metric("🎯 ATS Score", f"{score}%")

        with metric2:
            st.metric(
                "✅ Skills Matched",
                f"{len(resume_skills)}"
            )

        st.progress(score / 100)

        col3, col4 = st.columns(2)

        with col3:
            st.subheader("✅ Resume Skills")
            st.success(", ".join(resume_skills))

        with col4:
            st.subheader("❌ Missing Skills")

            if missing:
                st.error(", ".join(missing))
            else:
                st.success("No Missing Skills")

        st.subheader("📑 Resume Preview")
        st.text_area(
            "Extracted Resume Text",
            resume_text,
            height=300
        )

        st.subheader("💡 AI Suggestions")

        if score >= 80:
            st.success(
                "Excellent resume match for this role."
            )
        elif score >= 50:
            st.warning(
                "Good match. Add missing skills to improve ATS score."
            )
        else:
            st.error(
                "Low match score. Improve resume with required skills."
            )

elif page == "Available Jobs":

    st.title("💼 Available Job Roles")

    data = []

    for role, skills in jobs.items():
        data.append({
            "Job Role": role,
            "Required Skills": ", ".join(skills)
        })

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Career Recommendation")

    st.info(
        "Choose a role based on your strongest skills and interests."
    )
