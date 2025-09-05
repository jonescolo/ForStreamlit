from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Initialize FastAPI app
app = FastAPI()

# Load Gemini using API key from environment variable
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Define POST endpoint for Excel or other clients
@app.post("/query")
async def query_endpoint(request: Request):
    body = await request.json()
    user_query = body.get("query", "")
    
    if not user_query:
        return JSONResponse(content={"error": "No query provided"}, status_code=400)
    
    try:
        response = llm.invoke(user_query)
        return JSONResponse(content={"response": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

