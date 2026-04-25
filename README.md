#  AI Resume Analyzer

An intelligent web application that analyzes resumes against job descriptions using AI, providing match scores, skill gaps, and actionable suggestions.

 **Live App:** https://ai-resume-analyzer-ykdsbejacguvgx8tgz73wz.streamlit.app/

---

##  Features

-  Upload resume (PDF)
-  AI-powered resume analysis
-  Match percentage calculation
-  Matching skills identification
-  Missing skills detection
-  Personalized improvement suggestions
-  Download analysis report

---

##  Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM API:** Groq (LLaMA 3.1)  
- **Libraries:**  
  - pdfplumber (PDF text extraction)  
  - re (text processing)  
  - openai (API client)

---

##  Project Structure

```
ai-resume-analyzer/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

##  Installation (Local Setup)

1. Clone the repository:
```
git clone https://github.com/Akash446-RM/ai-resume-analyzer.git
cd ai-resume-analyzer
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Create `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

4. Run the app:
```
streamlit run app.py
```

---

##  Environment Variables

| Variable | Description |
|----------|------------|
| GROQ_API_KEY | API key for Groq LLM |

 For deployment, use **Streamlit Secrets** instead of `.env`.

---

##  Deployment

Deployed using **Streamlit Community Cloud**

Steps:
1. Push code to GitHub  
2. Connect repository to Streamlit  
3. Add secret:
```
GROQ_API_KEY = "your_api_key_here"
```
4. Deploy  

---

##  Screenshots

_Add screenshots of your app here (recommended)_

---

##  Future Improvements

-  Advanced analytics dashboard  
- PDF report generation  
-  Keyword-based ATS optimization  
-  Multi-job comparison  
-  Resume rewriting suggestions  

---

##  Contributing

Contributions are welcome! Feel free to fork this repo and improve it.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

**Akash RM**  
 GitHub: https://github.com/Akash446-RM/ai-resume-analyzer

---

⭐ If you like this project, give it a star!
