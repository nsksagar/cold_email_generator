# Cold Email Generator

Generates personalized cold emails for job applications by matching a job posting against your portfolio data using a Large Language Model (LLM).

## How it works

1. Job details are read from a structured input (CSV).
2. Portfolio data is queried from a vector database to find relevant skills/links for that job.
3. An LLM drafts a personalized cold email using the job details + matched portfolio context.

## Tech Stack

- **LLM / Inference:** Groq API (LLaMA 3.3 70B)
- **Orchestration:** LangChain, LangGraph
- **Vector DB:** ChromaDB (semantic search over portfolio data)
- **Data handling:** pandas
- **Config:** python-dotenv

## Project Structure

```
cold_email_generator/
├── app/                       # Application code (env config, core scripts)
├── check_groq.ipynb           # Test/verify Groq API connectivity
├── check_chromaDB.ipynb       # Test/verify ChromaDB setup and queries
├── cold_email_generator.ipynb # Main pipeline: job data → portfolio match → email draft
├── projects.csv               # Portfolio/project data used for context matching
├── requirements.txt           # Python dependencies
└── .vscode/                   # Editor config
```

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/nsksagar/cold_email_generator.git
   cd cold_email_generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get a Groq API key from [console.groq.com/keys](https://console.groq.com/keys) and add it to a `.env` file in `app/`:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. Run `cold_email_generator.ipynb` to generate emails. Use `check_groq.ipynb` and `check_chromaDB.ipynb` to verify your API key and vector DB setup independently.

## Current Limitations

- Input must be provided as CSV (job listings, portfolio data).
- Input files must be manually placed in the working directory.

## Upcoming Improvements

- Support for resume PDF and portfolio link inputs (not just CSV)
- More flexible input handling
- Better automation for data ingestion/preprocessing

## License

Not specified.
