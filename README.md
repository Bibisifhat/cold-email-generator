📩 Cold Email Generator using LLMs

Generate personalized, human-like cold emails automatically from job postings using Large Language Models (LLMs).

This project extracts job details from a given URL and generates a concise, professional cold email tailored to the opportunity.


🚀 Live Demo

https://cold-email-generator-bibisifhat.streamlit.app/


🧠 How It Works

User pastes a job posting URL

The app scrapes the webpage content

Extracts structured job data using an LLM

Matches relevant skills from your project database

Generates a personalized cold email

Allows download of the generated email


🛠 Tech Stack

Streamlit – Web interface

LangChain – LLM orchestration

Groq (LLaMA 3.3 70B) – Language model

ChromaDB – Vector similarity search

Pandas – CSV data handling

BeautifulSoup – Web scraping


🔐 Environment Setup

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here


▶️ Run Locally

Clone the repository:
git clone https://github.com/Bibisifhat/cold-email-generator.git

cd cold-email-generator

Create virtual environment:
python -m venv venv

source venv/bin/activate  # macOS/Linux

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app/main.py


🌐 Deployment (Streamlit Cloud)
Push code to GitHub
Go to https://share.streamlit.io

Deploy using:
Repository: cold-email-generator
Main file: app/main.py

Add secret:
GROQ_API_KEY = "your_key_here"


✨ Features

Automatic job extraction from URLs

JSON-based structured parsing

Project-to-skill similarity matching using ChromaDB

Clean, word-wrapped email output

Downloadable email file


📌 Example Use Case

Instead of manually drafting emails for each internship or job:

Paste job URL

Generate tailored cold email

Edit if needed

Send

Saves time and improves personalization.


🧑‍💻 Author

Bibisifhat

3rd Year B.E Computer Engineering

Don Bosco College of Engineering, Fatorda

GitHub: https://github.com/Bibisifhat
