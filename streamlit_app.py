import streamlit as st
from langchain.llms import OpenAI

st.title("Excel Assistant")

query = st.text_input("Ask a question about your data:")
if query:
    llm = OpenAI(openai_api_key="your-openai-key")  # Replace with your key
    response = llm(query)
    st.write(response)
