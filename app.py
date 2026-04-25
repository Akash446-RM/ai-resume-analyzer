import streamlit as st
from openai import OpenAI
import pdfplumber
import re
import os

client = OpenAI(
   api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.markdown("""
<style>
html, body {
    background-color: #0e1117;
    color: white;
}

.header {
    text-align: center;
    padding: 20px;
}
.title {
    font-size: 42px;
    font-weight: bold;
    color: #4CAF50;
}
.subtitle {
    color: #bbb;
}

.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    margin-top: 10px;
    color: white;
    font-size: 18px;
    font-weight: 600;
}

textarea {
    color: white !important;
    background-color: #1c1f26 !important;
    border-radius: 10px !important;
}

textarea::placeholder {
    color: #888 !important;
}

.stButton>button {
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# 🔥 HEADER
st.markdown("""
<div class="header">
    <div class="title">🚀 AI Resume Analyzer</div>
    <div class="subtitle">Smart insights using AI</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
resume_text = ""

with col1:
    st.markdown('<div class="card"> Upload Resume</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

with col2:
    st.markdown('<div class="card"> Job Description</div>', unsafe_allow_html=True)
    job_desc = st.text_area("Enter Job Description", height=180)

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text

if st.button("Analyze Resume"):

    if resume_text and job_desc:

        with st.spinner("Analyzing..."):

            prompt = f"""
Compare the resume and job description.

Resume:
{resume_text}

Job Description:
{job_desc}

Return STRICTLY in this format:

Match Percentage: XX%

Matching Skills:
- ...

Missing Skills:
- ...

Suggestions:
- ...
"""

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

        st.success(" Analysis Complete")

        match = re.search(r'(\d{1,3})%', result)
        match_percent = int(match.group(1)) if match else 70

        st.subheader(" Match Score")
        st.progress(match_percent / 100)
        st.markdown(f"### {match_percent}% Match")

        sections = {
            "Matching Skills": "",
            "Missing Skills": "",
            "Suggestions": ""
        }

        current = None
        for line in result.split("\n"):
            if "Matching Skills" in line:
                current = "Matching Skills"
            elif "Missing Skills" in line:
                current = "Missing Skills"
            elif "Suggestions" in line:
                current = "Suggestions"
            elif current:
                sections[current] += line + "\n"

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Matching Skills")
            st.write(sections["Matching Skills"] or "—")

            st.markdown("###  Missing Skills")
            st.write(sections["Missing Skills"] or "—")

        with col2:
            st.markdown("###  Suggestions")
            st.write(sections["Suggestions"] or "—")

        st.download_button(
            label="Download Report",
            data=result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )

    else:
        st.warning(" Please upload resume and enter job description.")