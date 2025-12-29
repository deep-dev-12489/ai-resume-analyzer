import streamlit as st
import re

#App title
st.title("Resume Analyzer")

#Resume input 
resume_text = st.text_area("Give me your resume")

#Analyze button
if st.button("Analyze Resume"):
    #Check empty input
    if resume_text.strip() == "":
        st.warning("Please enter your resume text.")
    else:
        #Words & lines count
        words = resume_text.split()
        lines = resume_text.split('\n')

        #email extraction
        email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume_text)  

        phone = re.findall(r"\b\d{10}\b", resume_text)

        skills = re.findall(r"\b(Python|Java|C\+\+|JavaScript|SQL|HTML|CSS|Machine Learning|Data Analysis|Project Management)\b", resume_text)

        skilss = [ "Python", "Java", "C++", "JavaScript", "SQL", "HTML", "CSS", "Machine Learning", "Data Analysis", "Project Management"   
                  ]
        found_skills =[]
        for skill in skills:
            if skill in resume_text.lower():
                found_skills.append(skill)
        # Output section
        st.subheader("📊 Resume Analysis Result")

        st.write("Total Words:", len(words))
        st.write("Total Lines:", len(lines))

        st.write("Email:", email[0] if email else "Not found")
        st.write("Phone:", phone[0] if phone else "Not found")

        st.write("Skills Found:", found_skills if found_skills else "None")

        # Resume score
        score = len(found_skills) * 10
        st.write("Resume Score:", score, "/ 100")      
