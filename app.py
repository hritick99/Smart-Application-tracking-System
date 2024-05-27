import streamlit as st
import google.generativeai as genai
import os 
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_text(upload):
    reader = pdf.PdfReader(upload)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text



input_prompt="""
Hey act like a skilled or very experience ATS(application tracking system)
with a deep understanding of tech fields,software engineering,data science,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description
.You must consider the job market is very competitive and you should provide best assistance for improving the resumes.Assign the percentage Matching based on the JG asd the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having tje structure
{{"JD Match":"%","MissingKeywords:[]","Profile summary":""}}
"""   

st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job description")
upload=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

submit=st.button("Submit")

if submit:
    if upload is not None:
        text = input_pdf_text(upload)
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))

        # Parse response string into a dictionary
        response_dict = eval(response)  # Assuming the response is in valid dictionary format

        # Display the output in a Streamlit box with proper formatting
        st.write("JD Match: ", response_dict["JD Match"])
        st.write("Missing Keywords: ", response_dict["MissingKeywords"])
        st.write("Profile Summary: ", response_dict["Profile summary"])
        