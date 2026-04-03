April/2/2026

🚀 Cold Email Generator for Job Applications
This application automates the process of generating personalized cold emails for job applications based on job postings and your professional profile.
🔍 Overview
The system analyzes job descriptions and matches them with your portfolio data to generate tailored cold emails that highlight relevant skills and experiences.
Currently, the application:
Extracts job-related information from structured inputs (CSV files)
Uses your portfolio data to create context-aware email drafts
Leverages large language models to generate high-quality, personalized outreach messages
⚙️ Tech Stack
LLM: LLaMA 3.3 (70B Versatile)
Vector Database: ChromaDB (for semantic similarity and context retrieval)
Inference Backend: Groq (for accelerated LLM performance)
📂 Current Limitations
Requires input data (e.g., portfolio or job listings) to be provided in CSV format
Input files must be manually placed in the working directory
🔄 Upcoming Improvements
Support for multiple input formats:
your_resume.pdf
your_portfolios.csv
Portfolio links (e.g., GitHub, personal website)
More flexible and user-friendly input handling
Enhanced automation for data ingestion and preprocessing
💡 Goal
To simplify and scale the job application process by generating high-quality, personalized cold emails with minimal manual effort.




April/3/2026

**Recent Updates:**

Bug Fixes: Resolved an issue where the email generation output was displaying as `None` by ensuring the LLM response is properly returned to the main application block.

UI Improvements: Cleared the default testing URL from the Streamlit input field, providing a clean, blank text area for the user to input their target job links.

