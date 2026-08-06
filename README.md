# Laptop Recommendation Agent

An AI-powered laptop recommendation agent built with Python, LangChain, LangGraph, SQLite, and the eBay Browse API.

## Features

- AI agent using LangGraph
- Tool calling
- SQLite caching
- eBay Browse API integration
- Budget, brand, and RAM-based recommendations

## Tech Stack

- Python
- LangChain
- LangGraph
- Google Gemini / OpenAI
- SQLite
- eBay Browse API

## Project Structure

```
.
├── api.py              <-- FastAPI app
├── app.py              <-- Streamlit UI
├── agent.py
├── tools.py
├── llm.py
├── db.py
├── ebay.py
├── data.py
└── laptops.db
├── requirements.txt
└── README.md
```

## Run

```bash
pip3 install -r requirements.txt
# main.py is not updated to pass session_state.messages like in app.py
python3 main.py 

# Main commands to run frontend and backend
# Brings up fastAPI server in port 8000 by default
uvicorn api:app --reload
# Brings up UI
streamlit run app.py



# Check everything before pushing
black --check .
ruff check .
python -m compileall .

#To fix 
black .
ruff check . --fix
```

## Deploy backend (api.py) in Render

```
Start Command when Render Web Service is created :
uvicorn api:app --host 0.0.0.0 --port $PORT
#This tells Uvicorn:

Load the file api.py
Find the FastAPI object named app
Start serving it

So only api.py becomes the web server entry point, even though all files are present in the repository.

```

## Deploy frontend (apop.py) in Streamlit

```

Step 1: Push latest code to GitHub (appy.py and requirements.txt are main files which calls other files during runtime)

Step 2: Create Streamlit Cloud account . Go to: Sign in with GitHub (Authorize Streamlit to access your repositories)
https://share.streamlit.io/

Step 3: Create a new Streamlit app

```
Click 'Create app'
Deploy a public app from GitHub
Choose 
    Repository:
    tulasigudibanda/laptop-recommendation-agent
    Branch:
    main
    Main file path:
    app.py
Deploy

Step 4: Add secrets/environment variables
In Streamlit Cloud:
    App Settings -> Secrets
Add: 
OPENAI_API_KEY="your-key"
API_URL="https://laptop-recommendation-agent.onrender.com"   

Step 5: Deploy and test
Streamlit will build your app. You will get a URL like: 
https://laptop-recommendation-agent.streamlit.app


## Architecture

```

You effectively had two separate applications:

User input/Browser
    ↓
Streamlit UI/Streamlit Community Cloud (Frontend)
    ↓
requests.post(API_URL)
    ↓
FastAPI /chat endpoint
    ↓
LangGraph Agent
    ↓
OpenAI
    ↓
Response back to UI

```

