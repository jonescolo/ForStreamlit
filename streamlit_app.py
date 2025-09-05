
import streamlit as st
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.7,
    max_tokens=1024
)

st.title("Excel Assistant (Powered by Gemini)")

# Upload Excel or CSV file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "csv"])
if uploaded_file:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
    st.dataframe(df)

    # Create LangChain agent using Gemini
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        agent_type=AgentType.OPENAI_FUNCTIONS,  # Gemini supports function-style agents
        verbose=True,
        number_of_head_rows=df.shape[0]
    )

    # Ask a question
    query = st.text_input("Ask a question about your data:")
    if query:
        response = agent.run(query)
        st.write(response)





