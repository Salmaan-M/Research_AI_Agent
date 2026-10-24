# AI Research Assistant

A small command-line research assistant built with LangChain and Google Gemini. It can search the web, query Wikipedia, and return structured research summaries.

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file from `.env.example` and add your Google API key:

   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```

## Run

```powershell
python main.py
```

Enter a research question when prompted. The assistant prints a structured summary with sources and tools used.
