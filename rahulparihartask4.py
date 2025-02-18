# -*- coding: utf-8 -*-
"""RahulPariharTask4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dY4W90x6Z10uF7WZ2x8wlE9AQPtl7NMt
"""

import streamlit as st
from code_review import review_code
st.title("AI Code Reviewer (Gemini AI)")
code = st.text_area("Paste your Python code here:", height=200)
if st.button("Review Code"):
    if code.strip():
        response = review_code(code)
        st.subheader("Review Feedback")
        #st.subheader("Updated Code")
        st.write(response)
    else:
        st.warning("Please enter some Python code.")

import google.generativeai as genai
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCsXFgJ3f71_RACmoW-CPmAjQStzc5AMFg"
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def review_code(code):
    model = genai.GenerativeModel("gemini-1.5-pro")

    prompt = f"Analyze this Python code,if the code is correct do not give any review feedback and if the code is wrong then suggest the bug report and improvements:\n\n{code}"

    response = model.generate_content(prompt)

    return response.text