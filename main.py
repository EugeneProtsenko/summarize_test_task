from fastapi import FastAPI, HTTPException
import uvicorn
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import OpenAI
from langchain_core.documents import Document
from models import SummarizeRequest

app = FastAPI()



@app.get("/")
async def read_root():
    return {"message": "Welcome to the summarization API. Use the /summarize endpoint to get text summaries."}


@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text field is required")

    # Initialize the OpenAI LLM
    llm = OpenAI(model="gpt-3.5-turbo", openai_api_key="your_openai_api_key")

    # Load the summarization chain
    summarize_chain = load_summarize_chain(llm)

    # Wrap the input text in a Document object
    input_document = Document(page_content=request.text, metadata={})

    # Run the chain with the input document
    summary = summarize_chain.run([input_document])

    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
