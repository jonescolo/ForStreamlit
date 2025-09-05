
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

@app.post("/query")
async def query_endpoint(request: Request):
    body = await request.json()
    user_query = body.get("query", "")
    response = llm.invoke(user_query)
    return JSONResponse(content={"response": response})
