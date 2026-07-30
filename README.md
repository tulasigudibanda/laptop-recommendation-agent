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
├── main.py
├── agent.py
├── llm.py
├── tools.py
├── db.py
├── ebay.py
├── data.py
└── laptops.db
```

## Run

```bash
pip3 install -r requirements.txt
python3 main.py - not updated to pass session_state.messages like in app.py
streamlit run app.py
```
