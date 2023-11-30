import streamlit as st
from dotenv import load_dotenv
from utils import save_uploaded_file, process_uploaded_file, generate

load_dotenv(override=True)

st.set_page_config(
    page_title="AI-Based Blog generator",
    layout="wide",
)

st.title("AI-Based Blog generator")

st.sidebar.header("Upload document")
uploaded_file = st.sidebar.file_uploader(
    "Upload PDF", type=["pdf"])
if st.sidebar.button("Generate blog", type="primary", use_container_width=True):
    with st.spinner("Generating..."):
        file_path = save_uploaded_file(uploaded_file)
        docs = process_uploaded_file(file_path)
        res = generate(docs)
        st.sidebar.success("Blog generated successfully")
    st.write(res)
