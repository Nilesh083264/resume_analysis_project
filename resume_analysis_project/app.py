import streamlit as st
from resume_parser import parse_resume
from ml_model import load_model, predict_role
import os

st.title("📄 Resume Analysis & Classification using GenAI Powered Bu -Nilesh  Shirgire")

uploaded_file = st.file_uploader("Upload Resume (PDF, DOCX, or Image)", type=["pdf", "docx", "png", "jpg", "jpeg"])

if uploaded_file:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text, gap = parse_resume(uploaded_file.name)
    st.subheader("Extracted Resume Text:")
    st.text_area("Text", text, height=250)

    model, vectorizer = load_model()
    role = predict_role(text, model, vectorizer)

    st.success(f"Predicted Role: {role}")
    if gap:
        st.warning("⚠️ Education gap detected in resume.")
    else:
        st.info("✅ No education gap detected.")

    os.remove(uploaded_file.name)