# FastAPI Text Summarizer

This is a simple web application that integrates an AI-powered text summarization service using FastAPI and LangChain. The application accepts text input from the user and returns a summarized version of the text.

## Setup

### Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
## Install Dependencies
```bash
pip install fastapi uvicorn langchain langchain-openai pydantic
```
## Running the Application
### Start the FastAPI Server
```bash
uvicorn main:app --reload
```
The application will be available at http://127.0.0.1:8000.

## API Endpoints
### GET /
Description: Root endpoint to check if the API is running.
Response:
json
{
  "message": "Welcome to the summarization API. Use the /summarize endpoint to get text summaries."
}
### POST /summarize

- **Description**: Endpoint to summarize the provided text.
- **Request**:
  - **Method**: POST
  - **URL**: `http://127.0.0.1:8000/summarize`
  - **Headers**: `Content-Type: application/json`
  - **Body**:
    ```json
    {
      "text": "Your text to summarize goes here."
    }
    ```
- **Response**:
  - **Body**:
    ```json
    {
      "summary": "Summarized text will be here."
    }
    ```

#### Example Usage

##### Using curl

```bash
curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d '{"text": "Your text to summarize goes here."}'
```
### Using Python requests

```
import requests

url = "http://127.0.0.1:8000/summarize"
data = {
    "text": "Your text to summarize goes here."
}
response = requests.post(url, json=data)
print(response.json())
```
## Using Postman
- Create a new POST request.
- Set the URL to http://127.0.0.1:8000/summarize.
- Go to the Headers tab and ensure Content-Type is set to application/json.
- Go to the Body tab, select raw, and choose JSON from the dropdown. Enter the JSON body:
```
{
    "text": "Your text to summarize goes here."
}
```
