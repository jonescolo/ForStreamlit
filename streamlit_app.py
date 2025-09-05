import streamlit as st
import pandas as pd
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent

# Load Excel file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "csv"])
if uploaded_file:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
    st.dataframe(df)

    # Create LangChain agent
    llm = OpenAI(openai_api_key="your-openai-key")  # Replace with your actual key
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    # Ask a question
    query = st.text_input("Ask a question about your data:")
    if query:
        response = agent.run(query)
        st.write(response)


